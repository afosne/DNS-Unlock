import json
import requests


with open('afosne.json') as file:
    data = json.load(file)


auth_email = 'afosnesub@afosne.icu'
#api申请
auth_key = 'd79573993130b741718d68b72eda4af6736a7'
#账户ID
identifier = '9ab8c1e34fdf3ae7ecdc06cde6e6e7b9'

headers = {
    'X-Auth-Email': auth_email,
    'X-Auth-Key': auth_key,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

for item in data:
    hostname = item['hostname']
    for ip in item['ips']:
        payload = json.dumps({
            "action": "override",
            "filters": ["dns"],
            "description": f"{hostname}",
            "enabled": True,
            "name": hostname,
            "rule_settings": {
                "override_host": ip
            },
            "traffic": f"any(dns.domains[*] == \"{hostname}\")"
        })

        url = f"https://api.cloudflare.com/client/v4/accounts/{identifier}/gateway/rules"
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
