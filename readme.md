#依赖  
    pip install flask  
    pip install flask_restful  
    pip install gevent  
#mysql  
root 登录  
mysql -u root -p  
创建 数据库  
CREATE DATABASE 名称;  
删除数据库  
drop database <数据库名>;  
为远程主机授予登录权限  
grant select,update,insert,delete on *.* to root@192.168.132.79 identified by "1000";  
