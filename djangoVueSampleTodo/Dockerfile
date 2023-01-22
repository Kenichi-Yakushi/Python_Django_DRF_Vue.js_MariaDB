# pull official base image
FROM python:3.9-slim-buster

WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get clean
RUN apt-get -y install gcc libmariadb-dev

RUN pip install --upgrade pip
RUN pip install django
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install urllib3
# 日記アプリ用
RUN pip install django-allauth
RUN pip install django-bootstrap5

# install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# add app
# COPY . .