import json

# 打开 TXT 文件并读取数据
with open('dnstest.txt', 'r') as file:
    txt_data = file.read()

# 假设 TXT 文件中的数据是简单的 CSV 格式，我们可以这样解析
# 如果数据格式更复杂，可能需要更复杂的解析逻辑
data = txt_data.strip().split('\n')
rows = [row.split(',') for row in data]

# 将解析后的数据转换为字典列表
# 假设第一行是列名
headers = rows[0]
data_dicts = [dict(zip(headers, row)) for row in rows[1:]]

# 转换为 JSON 格式
json_data = json.dumps(data_dicts, indent=4)
print(json_data)
