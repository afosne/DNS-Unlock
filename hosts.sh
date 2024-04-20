#!/bin/bash
# 指定包含主机列表的逗号拼接的字符串
hostlist="$@"
IFS='192.131.142.22,1.65.197.41,154.3.39.162,45.78.21.247,103.177.248.249,101.36.109.26,149.129.94.159,8.218.63.116,1.65.218.124,46.20.109.51' read -ra hosts <<< "$hostlist"
for host in "${hosts[@]}"
do
  curl -s -o /dev/null -m 1 -H "Host:www.netflix.com" -w "$host\t%{http_code}\t%{time_total}\n" http://$host
done
