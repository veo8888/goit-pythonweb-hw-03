FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/storage

EXPOSE 3000

VOLUME ["/app/storage"]

CMD ["python", "app.py"]