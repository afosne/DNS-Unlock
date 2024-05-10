import json

# 读取文件内容
with open('dnstest.txt', 'r') as file:
    lines = file.readlines()

results = []

# 解析每一行的数据
for line in lines:
    parts = line.split()
    if len(parts) == 4:
        domain = parts[0].rstrip('.')
        ttl = parts[1]
        record_type = parts[2]
        ip = parts[3]
        result = {
            "domain": domain,
            "ttl": ttl,
            "type": record_type,
            "ip": ip
        }
        results.append(result)

# 保存为json文件
with open('output.json', 'w') as file:
    json.dump(results, file, indent=2)
