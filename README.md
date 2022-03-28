# Быстрый старт 
В папку проекта клонируем исходник
```commandline
git init
git remote add origin https://github.com/imoknot/suslig
git pull origin master
```

#### Для локальной разрабоки
Установить зависимости 
```commandline
pip install -r requirements.txt
```

#### Для докера  
```
Dockerfile
docker build -t suslig .
docker run -d --name susligdok -p 80:80 suslig
```

# Настройка сервера для ручной сборки 

### Если нужно русифицировать сервер 
```
sudo dpkg-reconfigure locales - > UTF-8.ru
```

### Папочка для проекта
```
sudo mkdir /var/www/suslig 
cd /var/www/suslig
sudo chown 
```
не забываем ставить нужные права на папку

Clone suslig and all requirements



Create virtual environment
```
$ virtualenv -p python3.9 venv
$ mkdir app
$ . venv/bin/activate
(venv) $ cd app
```




test application 
```buildoutcfg
python3 run.py
```
```
INFO:     Started server process [23416]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
if all ok - start application on gunicorn
```
(venv) $ gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

### Configure Nginx
```
$ sudo nano /etc/nginx/sites-available/suslig
```

```
server{
       server_name <your-site-name>;
       location / {
           include proxy_params;
           proxy_pass http://127.0.0.1:8000;
       }
}
```
make a symbolic link to this config file
```
$ sudo ln -s /etc/nginx/sites-available/suslig /etc/nginx/sites-enabled/
```
restart nginx

``` buildoutcfg
$ sudo systemctl restart nginx.service
```

### Start daemon
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
``` buildoutcfg
sudo systemctl start suslig.service
````
