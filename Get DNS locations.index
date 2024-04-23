var myHeaders = new Headers();
myHeaders.append("X-Auth-Email", "7920a9c2@gmail.com");
myHeaders.append("X-Auth-Key", "d79573993130b741718d68b72eda4af6736a7");
myHeaders.append("User-Agent", "Apifox/1.0.0 (https://apifox.com)");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
   "ips": [
      "192.0.2.1/32"
   ],
   "name": "${YouDnsName}"
});

var requestOptions = {
   method: 'POST',
   headers: myHeaders,
   body: raw,
   redirect: 'follow'
};

fetch("https://api.cloudflare.com/client/v4/accounts/b9026a15a586c9fbdd6d8ee2947a8cdb/gateway/locations", requestOptions)
   .then(response => response.text())
   .then(result => console.log(result))
   .catch(error => console.log('error', error));
