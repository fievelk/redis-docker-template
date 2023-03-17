# syntax=docker/dockerfile:1
FROM python:3.11-alpine
WORKDIR /src

ENV FLASK_APP=redis_experiments/receiver_service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
