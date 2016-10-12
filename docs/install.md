# install
## nginx
```
sudo rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
sudo yum install nginx
sudo chkconfig nginx on
sudo service nginx restart
```

## python3
```
sudo yum install gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel git
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
vi .bash_profile
source .bash_profile
pyenv install 3.5.1
pyenv global 3.5.1
pyenv rehash
pip install tornado
```