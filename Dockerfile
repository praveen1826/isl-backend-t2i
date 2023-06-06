FROM python:3.11.3-alpine

RUN mkdir -p /home/islBackendT2I

WORKDIR /home/islBackendT2I

COPY . .

RUN apk update

RUN pip install django djangorestframework pillow django-debug-toolbar

RUN apk add --virtual build-deps gcc python3-dev musl-dev

RUN apk add --no-cache mariadb-dev

RUN pip install mysqlclient

CMD ["python" , "manage.py" , "runserver" , "0.0.0.0:8000"]