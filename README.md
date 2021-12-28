## Hi! 

Light and fast content CMS Suslig
Based on FastAPI, PostgreSQL and SQLAlchemy  

https://suslig.ru/ 


## Fast start. 

### Create folders
```
$ mkdir /var/www/suslig 
$ cd /var/www/suslig
```

Create virtual environment
```
$ virtualenv -p python3.9 venv
$ mkdir app
$ . venv/bin/activate
(venv) $ cd app
```


Clone suslig and all requirements

```
(venv) $ git init
(venv) $ git remote add origin https://github.com/imoknot/suslig
(venv) $ git pull origin master
(venv) $ pip install -r requirements.txt

```

### Configure Nginx
for Debian
```
(venv) $ deactivate
$ sudo nano /etc/systemd/system/suslig.service
```
edit this file 
<UserName> - your system name
<processor core +1> - recommendation from the gunicorn manual. For 8 core CPU = 8+1 = 9

```
[Unit]
Description=Gunicorn instance to serve Suslig
After=network.target

[Service]
User=<UserName>
Group=www-data
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TasksMax=infinity

RuntimeDirectory=gunicorn
WorkingDirectory=/var/www/suslig
ExecStart=/var/www/suslig/venv/bin/gunicorn -w <processor core +1> -k uvicorn.workers.UvicornWorker app:app

[Install]
WantedBy=multi-user.target
```
Done! Run your python application.
```
sudo systemctl start suslig.service
````