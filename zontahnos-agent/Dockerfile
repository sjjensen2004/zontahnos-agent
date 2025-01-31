FROM python:3.11-slim

WORKDIR /app 
COPY ./app/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app/app ./app
WORKDIR /app/app
COPY config.yaml ./core
ENV PYTHONPATH=/app

CMD ["python", "main.py"]