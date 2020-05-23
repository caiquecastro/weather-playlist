from .cache import cache

class Stats:
    def register_access(self, city):
        cache.increment_by('access', 1, city)

    def top_access(self):
        return cache.get_range('access', 0, -1)

stats_service = Stats()
