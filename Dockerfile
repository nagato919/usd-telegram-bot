FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY usd_bot.py .

CMD ["python", "usd_bot.py"]
