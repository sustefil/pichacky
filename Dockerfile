FROM python:3.11-slim-bookworm

RUN apt update && apt install -y default-libmysqlclient-dev gcc g++ make sqlite3 curl

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY manage.py .
COPY src ./src

EXPOSE 8000
