# Быстрый старт 
В папку проекта клонируем исходник
```commandline
git init
git remote add origin https://github.com/imoknot/test_ii
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
docker run -d --name test_doker -p 80:80 test_ii
```
