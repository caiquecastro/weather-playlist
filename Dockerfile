FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app