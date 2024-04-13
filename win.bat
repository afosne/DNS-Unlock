@echo off  

rem //设置变量   
set DNS1=141.11.75.124


echo 当前可用操作有：  
echo   1 设置以太网DNS代理
echo   2 设置以太网DNS代理
echo   3 恢复动态DNS
echo   4 退出  
echo   .
echo 请选择后回车：  
set /p operate=  
if %operate%==1 goto 1  
if %operate%==2 goto 2  
if %operate%==3 goto 3  
if %operate%==4 goto 4  


:1
echo . 
echo 正在设置本地DNS代理，请稍等...  
echo 网络 = 以太网   
echo DNS  = %DNS1%   
echo .
netsh interface ipv4 set dns name=以太网 source=static addr=%DNS1% register=PRIMARY   
echo 本地代理已设置！  
pause  
goto 4 

:2
echo . 
echo 正在设置本地DNS代理，请稍等...  
echo 网络 = VLAN   
echo DNS  = %DNS1%   
echo .
netsh interface ipv4 set dns name=VLAN source=static addr=%DNS1% register=PRIMARY   
echo 本地代理已设置！  
pause  
goto 4 

:3  
echo .
echo 正在恢复动态DNS，请稍等...  
echo 网络 = %NAME%
echo .
netsh interface ip set dns name=%NAME% dhcp
echo 恢复动态DNS设置！  
pause  
goto 4  

:4  
exit