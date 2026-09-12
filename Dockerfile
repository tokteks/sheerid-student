# SheerID Student Bot — Dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py bot.py
COPY bot_railway.py bot_railway.py
COPY tools/ tools/

CMD ["python", "bot.py"]