# https://realpython.com/python-redis/
import redis

r = redis.Redis(port=6379,
                #host='redis'
                )

r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(r.get("Bahamas"))

print(r.get("hits"))