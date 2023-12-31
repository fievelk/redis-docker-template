# Dockerized Redis Template

This repository is a very basic template that shows how two services can communicate with each other using Redis as their intermediary. Feel free to use it as a starting point for studying or experimenting.

- [Running the project](#running-the-project)
  - [Requirements](#requirements)
- [Checking the contents of the Redis server](#checking-the-contents-of-the-redis-server)


## Running the project

It's necessary to have **Docker** and **Docker Compose** on your system. Once these are set up, just give the following command from the root folder:
```sh
docker compose up
```

At this point, you should have two webservers running on these addresses:
- http://localhost:8000 (sender)
- http://localhost:8001 (receiver)

The Sender and the Receiver are two simple webservers implemented using Flask. Visiting the sender URL will send some data to the Redis server and show it on the page. Visiting the receiver URL will fetch the data from Redis and show it. Every time you refresh the sender page, new data will be added to the Redis list.


### Requirements

As long as you can run docker and docker compose, you don't need to worry about requirements. If you're curious, know that there are two different types of requirements:
- `pyproject.toml` (Poetry requirements): dependencies used for local development (e.g. `black`).
- `requirements.txt`: dependencies needed by the containers.


## Checking the contents of the Redis server

We can access the Redis server directly to check what's going on:
```console
$ redis-cli -h localhost -p 6379
localhost:6379> KEYS *
1) "my-lists"
localhost:6379> LRANGE my-lists 0 -1
1) "three"
2) "two"
3) "one"
```
