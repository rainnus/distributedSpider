import redis

r = redis.Redis()

# r.delete(["blogSpider1:items"])
# r.delete(["blogSpider1:dupefilter"])
# r.delete(["blogSpider1:request"])
r.flushall()