import json
import requests

# 假设你的JSON文件名为'ips.json'
with open('ips.json', 'r') as file:
    data = json.load(file)

ips_dict = {}

# 遍历JSON数据
for item in data:
    hostname = item['hostname']
    ips = item['ips']
    for ip in ips:
        # 检查状态码
        response = requests.get(f'http://{ip}')
        if response.status_code == 503:
            # 保留状态为503的IP
            ips_dict[hostname] = ip

# 删除非503状态的IP
ips_to_remove = {ip: hostname for hostname, ip in ips_dict.items() if ip not in data[hostname]['ips']}
for ip, hostname in ips_to_remove.items():
    del ips_dict[hostname]

# 以域名-IP格式重新构建数据
filtered_ips = {hostname: [ip] for hostname, ip in ips_dict.items()}

# 保存到新的JSON文件
with open('503_filtered_ips.json', 'w') as f:
    json.dump(filtered_ips, f, indent=2)

print(f'JSON数据已保存到 "503_filtered_ips.json" 文件中')
