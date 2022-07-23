from django.core.cache import cache
from typing import Any


class CacheController:

    def __init__(self, cache_name: str):
        self.name = cache_name
        self.urls = []

    def save(self, data: Any, url: str, id_for_cache: str | None):
        cache_name_for_save = f'{self.name}-{url}-{id_for_cache}' if id_for_cache else f'{self.name}-{url}'
        cache.set(cache_name_for_save, data, None)
        self.urls.append(cache_name_for_save)

    def delete(self):
        none_cache = { url: None for url in self.urls }
        if len(none_cache.keys()) > 0:
            cache.set_many(none_cache)



bill_cache = CacheController('bill')