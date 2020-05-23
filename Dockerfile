FROM tiangolo/uvicorn-gunicorn:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
