FROM python:3.11-slim-bookworm

RUN apt update && apt install -y default-libmysqlclient-dev gcc g++ make

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
