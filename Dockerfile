FROM ubuntu:22.04

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ="Asia/Taipei"
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install python 3.10
RUN apt-get update -y
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install python3.10 python3.10-dev wget -y

# # Install PostgresSQL
RUN apt-get -y install gcc
RUN apt-get update && apt-get -y install postgresql libpq-dev postgresql-client postgresql-client-common 
RUN apt-get update && apt-get -y install python3-psycopg2 gettext

# Install pip
RUN apt-get install curl -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.10 get-pip.py
RUN pip install pip==23.0.1  # 使用兼容的 pip 版本

# set work directory
RUN mkdir -p /opt/app
COPY . /opt/app

RUN pip install -r /opt/app/requirements.txt

RUN chmod +x /opt/app/docker-entrypoint.sh
ENTRYPOINT [ "/opt/app/docker-entrypoint.sh" ]
