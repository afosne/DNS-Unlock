import requests
import json

# 获取"https://dnsip.afosne.workers.dev/?domain=netflix.com"返回的IP
response = requests.get("https://dnsip.afosne.workers.dev/?domain=netflix.com")
if response.status_code == 200:
    api_ip = response.json()["ip"]
else:
    print("Failed to retrieve IP from the API")
    api_ip = None

# 假设你有一个包含IP地址的JSON数据，名为json_data
# 你需要将json_data替换为实际的JSON数据
# 示例JSON数据格式：{"ip": "123.456.789.012"}
json_data = '{"ip": "123.456.789.012"}'

# 解析JSON数据中的IP地址
try:
    parsed_json = json.loads(json_data)
    json_ip = parsed_json["ip"]
except json.JSONDecodeError:
    print("Failed to parse JSON data")
    json_ip = None
except KeyError:
    print("IP address not found in JSON data")
    json_ip = None

# 比较两个IP地址
if api_ip and json_ip and api_ip == json_ip:
    print("Success: IP addresses match")
else:
    print("Failure: IP addresses do not match")
