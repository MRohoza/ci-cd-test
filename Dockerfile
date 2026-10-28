FROM python:3.12-slim
WORKDIR /app
COPY file_that_does_not_exist.py .
CMD ["python", "-u", "app.py"]
