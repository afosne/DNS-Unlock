@echo off  

rem //设置变量   
set NAME="本地连接"  
set DNS1=141.11.75.124


echo 当前可用操作有：  
echo   1 设置本地DNS代理
echo   2 恢复动态DNS
echo   3 退出  
echo   .
echo 请选择后回车：  
set /p operate=  
if %operate%==1 goto 1  
if %operate%==2 goto 2  
if %operate%==3 goto 3  

:1
echo . 
echo 正在设置本地DNS代理，请稍等...  
echo 网络 = %NAME%   
echo DNS  = %DNS1%   
echo .
netsh interface ipv4 set dns name=%NAME% source=static addr=%DNS1% register=PRIMARY   
echo 本地代理已设置！  
pause  
goto 3  


:2  
echo .
echo 正在恢复动态DNS，请稍等...  
echo 网络 = %NAME%
echo .
netsh interface ip set dns name=%NAME% dhcp
echo 恢复动态DNS设置！  
pause  
goto 3  

:3  
exit