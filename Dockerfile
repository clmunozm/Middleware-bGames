# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Instalar las dependencias incluyendo gunicorn
RUN pip install flask requests gunicorn flask-cors

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "middleware:app"]
