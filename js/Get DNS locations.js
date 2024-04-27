var myHeaders = new Headers();
myHeaders.append("X-Auth-Key", "${cf_api}"); //你的cloudflare api密钥
myHeaders.append("X-Auth-Email", "${cf_mail}"); //你的cloudflare 邮箱
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
   "ips": [
      "192.0.2.1/32"
   ],
   "name": "${Dns_Name}"
});

var requestOptions = {
   method: 'POST',
   headers: myHeaders,
   body: raw,
   redirect: 'follow'
};

fetch("https://api.cloudflare.com/client/v4/accounts/${account_id}/gateway/rules", requestOptions)
   .then(response => response.text())
   .then(result => console.log(result))
   .catch(error => console.log('error', error));
