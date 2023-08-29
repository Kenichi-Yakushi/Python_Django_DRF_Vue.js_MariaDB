# pull official base image
FROM python:3.9-slim-buster

# 作業ディレクトリを設定
WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# requirements.txtをコンテナ内の/usr/srcディレクトリにコピー
COPY requirements.txt .

# install system dependencies
RUN apt-get update \
    && apt-get clean
RUN apt-get -y install gcc libmariadb-dev

# requirements.txtの内容に基づいてパッケージをインストール
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install urllib3

# アプリケーションの残りの部分をコピー
COPY . .