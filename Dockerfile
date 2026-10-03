# Day 7: containerise the finished bot.
#
# Finished behaviour: small image, non-root user, dependencies cached in their
# own layer, SQLite stored on a mounted volume, secrets via environment.
#
#   docker build -t quartermaster .
#   docker run -d --restart unless-stopped --env-file .env \
#       -v quartermaster-data:/data -e DATABASE_PATH=/data/quartermaster.sqlite3 quartermaster
#
# This file is intentionally a working skeleton; review each line and decide
# whether you agree with it (that is the exercise).
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY quartermaster ./quartermaster

RUN useradd --create-home bot && mkdir /data && chown bot /data
USER bot

CMD ["python", "-m", "quartermaster"]
