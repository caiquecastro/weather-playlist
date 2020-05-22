import redis
from ..core.config import settings

class Cache:
    def __init__(self):
        self.redis = redis.Redis(host=settings.CACHE_HOST)

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value, expire=None):
        return self.redis.set(key, value, ex=expire)

cache = Cache()