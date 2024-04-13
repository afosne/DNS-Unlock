@echo off
setlocal enabledelayedexpansion



echo 1. 使用WLAN时更改任何使用的DNS到该服务
echo 2. 取消该服务
set /p choice=Enter your choice (1 or 2):

if "%choice%" == "1" (
 netsh interface ip add dnsserver name="WLAN" address=141.11.75.124
    echo DNS settings updated for adapter: !adapterName!
) else if "%choice%" == "2" (
 netsh interface set interface name="WLAN" admin=DISABLED
 netsh interface set interface name="WLAN" admin=ENABLED
 netsh interface ip set address name="WLAN" source=dhcp
) else (
    echo Invalid choice. Please select 1 or 2.
)

pause
endlocal
