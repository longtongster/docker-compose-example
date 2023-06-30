# docker-compose-example

This repo is intendend to learn docker-compose. It is used to code along with 

https://docs.docker.com/compose/gettingstarted/

In this example redis is used as an example to store the number of times the site has been visited.
For this a redis container will be started. You can configure to run the redis container to listen op port 6379.
When using docker compose the services can communicate via the name of their services.

## method 1

Run only with a redis container. In `app.py` comment out the `host='redis'`  argument of the `redis.Redis()` call.
This is required since we do not cannot call a container network called `redis`.

`docker container run -d --name redis -p 6379:6379 redis`

Then run the ` app.py` application.
 
## Without docker-compose

Please make sure that the argument in the redis call is set to `host='redis`. 
This is required since we will make use of a custom network this time.

The following steps can be followed:
1. create a network called `redis` using
   `docker network create redis`
2. Launch a redis container in the network and with ports exposed
   docker run --name redis --network redis -p 6379:6379 -d redis
3. Launch a graphical interface to check if data is indeed added using
   docker run --name redis-commander --network redis -p 8081:8081 -d -e REDIS_HOST=redis rediscommander/redis-commander
4. build the container using the docker file in the app directory
   `docker image build -t flask-app .` Do not forget the dot.
5. Launch a container from the flask-app image
   `docker container run --name flask-app --network redis -p 5000:5000 -d flask-app`

The app can be found under `http:/localhost:5000`. Reloading will increase the count.
You can check the data inside the redis container by opening the webbrowser on `http:/localhost:8081`

## With docker-compose
With docker-compose both the redis container AND the simple app can be started with one command.
Here we follow the steps from the docker tutorial (see above).




#### extra
In the directory `quick-redis` is a very simple script that connects to redis, adds and retreives some data. 
You can use the grapical interface to see the data in the webbrowser


