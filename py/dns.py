import requests
import dns.resolver

# 设置要解析的域名列表和DoH服务器地址
domains = ["example.com", "google.com", "github.com"]
doh_server = "https://cloudflare-dns.com/dns-query"

try:
    # 创建DoH解析器
    resolver = dns.resolver.Resolver(configure=False)
    resolver.resolver.use_doh_servers = True
    resolver.resolver.doh_url = doh_server

    # 遍历域名列表
    for domain in domains:
        # 获取IP地址
        ip_address = resolver.resolve(domain, 'A')[0].to_text()

        # 发送HTTP请求
        response = requests.get(f"http://{ip_address}")

        # 检查响应状态码
        if response.status_code == 200:
            # 如果状态码是200（正常响应），则检查响应内容
            if "Backend not available" in response.text:
                print(f"Domain {domain} at IP {ip_address} shows 'Backend not available'")
            else:
                print(f"Domain {domain} at IP {ip_address} does not show 'Backend not available'")
        else:
            print(f"Error while resolving {domain}: {response.status_code}")

except dns.resolver.NXDOMAIN:
    print(f"Domain {domain} does not exist")
except dns.resolver.Timeout:
    print(f"Timeout occurred while resolving {domain}")
except Exception as e:
    print(f"Error occurred: {e}")
