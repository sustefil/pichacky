FROM python:3.11-slim-bookworm

RUN apt update && apt install -y default-libmysqlclient-dev gcc g++ make sqlite3

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000
