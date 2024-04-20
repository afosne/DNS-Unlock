// 使用时，替换hostText中的文本，一行一个域名。
var hosts = `\
        netflix.com
        netflix.net
        nflximg.com
        nflximg.net
        nflxvideo.net
        nflxso.net
        nflxext.com
`;
//替换ip为上一步筛选的ip
var ip = '1.2.3.4'
// 将hosts文本按行分割成数组
var hostLines = hosts.trim().split('\n');
// 初始化一个空数组来存储结果
var formattedHosts = [];

// 遍历每一行，添加为指定格式的文本
hostLines.forEach(function (hostname) {
  if (hostname.trim() !== '') {
    var formattedLine = `||${hostname}^$dnsrewrite=${ip}`;
    formattedHosts.push(formattedLine);
  }
});
// 将结果输出为文本
var formattedText = formattedHosts.join('\n');
console.log(formattedText); // 使用时，替换hostText中的文本，一行一个域名。
var hosts = `\
        netflix.com
        netflix.net
        nflximg.com
        nflximg.net
        nflxvideo.net
        nflxso.net
        nflxext.com
`;
//替换ip为上一步筛选的ip
var ip = '1.2.3.4'
// 将hosts文本按行分割成数组
var hostLines = hosts.trim().split('\n');
// 初始化一个空数组来存储结果
var formattedHosts = [];

// 遍历每一行，添加为指定格式的文本
hostLines.forEach(function (hostname) {
  if (hostname.trim() !== '') {
    var formattedLine = `||${hostname}^$dnsrewrite=${ip}`;
    formattedHosts.push(formattedLine);
  }
});
// 将结果输出为文本
var formattedText = formattedHosts.join('\n');
console.log(formattedText) > test.txt ;
