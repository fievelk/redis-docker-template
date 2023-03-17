import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


def _send_data(data: list):
    retries = 5
    while True:
        try:
            return cache.lpush("my-lists", *data)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def index():
    data = ["one", "two", "three"]
    count = _send_data(data)
    return f"Service 1 sent some data to Redis: {data}"
