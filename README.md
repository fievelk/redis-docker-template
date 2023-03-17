# Sharing data between services using Redis

This repository shows how two services can communicate with each other using Redis as their intermediary. Feel free to use it as a starting point for studying or experimenting with more advanced projects.

- Sender: sends data to Redis
- Receiver: fetches data from Redis

The Sender and the Receiver services are just two simple webservers implemented using Flask.


## Running the project

It's necessary to have docker and docker-compose on your system. Once these are set up, just give the following command from the root folder:
```sh
docker compose up
```

At this point, you should have two webservers running on two URLs:
- `http://localhost:8000` (sender)
- `http://localhost:8001` (receiver)

Visiting the sender URL will send some data to the Redis server and show it on the page. Visiting the receiver URL will fetch and show the data from Redis.

## Requirements

As long as you can run docker and docker compose, you don't need to worry about requirements. If you're curious, know that there are two different types of requirements:
- Poetry requirements: define the dependencies used by the host (like `black`).
- `requirements.txt`: defines the dependencies needed by the containers.
