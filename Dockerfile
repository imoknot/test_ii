# Для ручной настройки
# FROM python:3.10
# Для дефолта готовый образ
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.start:app", "--host", "0.0.0.0", "--port", "80"]