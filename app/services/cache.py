import json
import redis
import logging
from ..core.config import settings


logger = logging.getLogger(__name__)


class Cache:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL)

    def get(self, key):
        logger.debug(f'Fetching cached value for {key}')

        value = self.redis.get(key)

        if value is None:
            return None

        return json.loads(value)

    def set(self, key, value, expire=None):
        logger.debug(f'Saving cached value for {key}')

        return self.redis.set(key, json.dumps(value), ex=expire)

    def increment_by(self, key, amount, value):
        return self.redis.zincrby(key, amount, value)

    def get_range(self, key, start, end, with_scores=True):
        result = self.redis.zrevrange(
            key,
            start,
            end,
            withscores=with_scores
        )

        if not with_scores:
            return result

        return [{
            'key': key,
            'value': value,
        } for key, value in result]


cache = Cache()
