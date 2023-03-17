import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


def _receive_data():
    retries = 5
    while True:
        try:
            return cache.lrange("my-lists", 0, -1)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def index():
    received_data = _receive_data()
    return f"Service 2 read this data from Redis: {received_data}"
