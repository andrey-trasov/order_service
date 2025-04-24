FROM python:3.12.10-alpine3.21

COPY requirements.txt /temp/requirements.txt
COPY . /telegram
WORKDIR /telegram
EXPOSE 8001

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-adduser

USER service-adduser