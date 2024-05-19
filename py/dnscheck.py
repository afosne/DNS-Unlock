import requests
import json

# API URLs
api_urls = [
    'https://dnstest.afosnesub.workers.dev/afosne',
    'https://dnstest.afosnesub.workers.dev/afosnec',
    'https://dnstest.afosnesub.workers.dev/afosna'
]

for api_url in api_urls:
    # 获取JSON数据
    response = requests.get(api_url)
    data = response.json()

    # 初始化存储字典
    ips_dict = {}

    # 遍历API数据
    for item in data:
        if 'hostname' in item:
            hostname = item['hostname']
        elif 'domain' in item:
            hostname = item['domain']
        else:
            continue

        if 'ips' in item or 'ip_addresses' in item:
            # 检查IP列表是否为requests对象
            if isinstance(item['ips'], list) or isinstance(item['ip_addresses'], list):
                for ip in item['ips']:
                    try:
                        # 检查IP是否为requests对象
                        ip_response = requests.get(f'http://{ip}')
                        if ip_response.status_code == 503:
                            if hostname not in ips_dict:
                                ips_dict[hostname] = []
                            ips_dict[hostname].append(ip_response)
                    except requests.exceptions.RequestException:
                        # 如果请求失败,跳过该IP
                        continue
            else:
                continue

    # 删除非503状态的IP
    ips_to_remove = {ip: hostname for hostname, ip_list in ips_dict.items() if not any(response.status_code == 503 for response in ip_list if isinstance(response, requests.Response))}
    for ip, hostname in ips_to_remove.items():
        del ips_dict[hostname]

    # 以域名-IP格式重新构建数据
    filtered_ips = {hostname: [response.url.split('//')[-1] for response in ip_list] for hostname, ip_list in ips_dict.items() if ip_list}

    # 保存到新的JSON文件
    file_name = f'{api_url.split("/")[-1]}_503_filtered_ips.json'
    with open(file_name, 'w') as f:
        json.dump(filtered_ips, f, indent=2)

    print(f'JSON数据已保存到 "{file_name}" 文件中')
