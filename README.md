# docker-compose-example

This repo is intendend to learn docker-compose. It is used to code along with 

https://docs.docker.com/compose/gettingstarted/

In this example redis is used as an example to store the number of times the site has been visited.
For this a redis container will be started. You can configure to run the redis container to listen op port 6379.
When using docker compose the services can communicate via the name of their services.

## Without docker-compose

Without using docker compose you can:
1. create a network called `redis` using
   `docker network create redis`
2. Launch a redis container in the network and with ports exposed
   docker run --name redis --network redis -p 6379:6379 -d redis
3. Launch a graphical interface to check if data is indeed added using
   docker run --name redis-commander --network redis -p 8081:8081 -d -e REDIS_HOST=redis rediscommander/redis-commander

In the directory `quick-redis` is a very simple script that connects to redis, adds and retreives some data. 
You can use the grapical interface to see the data in the webbrowser

#### remark
Without containerizing the simple script you cannot use the `redis` as a host.


