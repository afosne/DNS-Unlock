import requests
import json

# 假设你有一个包含IP地址的JSON数据，名为json_data
# 你需要将json_data替换为实际的JSON数据
# 示例JSON数据格式：{"ip": "123.456.789.012"}
json_data = '{"ip": "123.456.789.012"}'

# 解析JSON数据中的IP地址
try:
    parsed_json = json.loads(json_data)
    ip = parsed_json["ip"]
except json.JSONDecodeError:
    print("Failed to parse JSON data")
    ip = None
except KeyError:
    print("IP address not found in JSON data")
    ip = None

if ip:
    # 查询IP地址信息
    response = requests.get(f"http://ip-api.com/json/{ip}")
    if response.status_code == 200:
        ip_info = response.json()
        country = ip_info["country"]
        asn = ip_info["as"]
        print(f"IP: {ip}")
        print(f"Country: {country}")
        print(f"ASN: {asn}")
    else:
        print("Failed to retrieve IP information")
else:
    print("No IP address found in JSON data")
