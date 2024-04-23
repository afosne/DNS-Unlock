var myHeaders = new Headers();
myHeaders.append("X-Auth-Key", "${cf-api}"); //你的cloudflare api密钥
myHeaders.append("X-Auth-Email", "${cf-mail}"); //你的cloudflare 邮箱
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
   "action": "override",
   "filters": [
      "dns"
   ],
   "description": "Unblock websites like streaming media",
   "enabled": true,
   "name": "TW", //cf DNS 策略名称
   "rule_settings": {
      "override_ips": [
         "${proxy-ip1}", //需要解析的ip地址 可以通过 https://dnsip.afosne.workers.dev/?hostname=netflix.com&country=us借口获得
         "${proxy-ip2}"
      ]
   },
   "traffic": "any(app.type.ids[*] in {14}) and any(app.type.ids[*] in {11}) and any(app.ids[*] in {534 626 548 549 554 550 585})"
});

var requestOptions = {
   method: 'POST',
   headers: myHeaders,
   body: raw,
   redirect: 'follow'
};

fetch("https://api.cloudflare.com/client/v4/accounts/${account_id}/gateway/rules", requestOptions) //account_id = 你的账户id
   .then(response => response.text())
   .then(result => console.log(result))
   .catch(error => console.log('error', error));
