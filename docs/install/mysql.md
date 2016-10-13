# mysql
```
sudo rpm --import http://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html
sudo rpm -ihv http://dev.mysql.com/get/mysql57-community-release-el6-7.noarch.rpm
yum --disablerepo=\* --enablerepo='mysql57-community*' list available
sudo yum --enablerepo='mysql57-community*' install -y mysql-community-server
sudo chkconfig mysqld on
sudo service mysqld restart
sudo cat /var/log/mysqld.log | grep "temporary password"
pip install pymysql
pip install peewee
```

## mysql command
```
SET GLOBAL validate_password_length=4;
SET GLOBAL validate_password_policy=LOW;
set password for root@localhost=password('root');
CREATE DATABASE kawanado CHARACTER SET utf8mb4;
```