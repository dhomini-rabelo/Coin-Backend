from django.core.cache import cache
from typing import Any


class CacheController:

    def __init__(self, cache_name: str):
        self.name = cache_name
        self.urls: list[str] = []

    def get(self, url: str, id_for_cache: str | None = None) -> Any:
        return cache.get(self.get_cache_name_for_save(url, id_for_cache))

    def has_cache(self, url: str, id_for_cache: str | None = None) -> bool:
        return self.get_cache_name_for_save(url, id_for_cache) in self.urls

    def get_cache_name_for_save(self, url: str, id_for_cache: str | None = None) -> str:
        return f'{self.name}-{url}-{id_for_cache}' if id_for_cache else f'{self.name}-{url}'

    def save(self, data: Any, url: str, id_for_cache: str | None = None):
        cache_name_for_save = self.get_cache_name_for_save(url, id_for_cache)
        cache.set(cache_name_for_save, data, None)
        self.urls.append(cache_name_for_save)

    def delete_only(self, cache_name: str):
        if cache_name in self.urls:
            cache.set(cache_name, None)
            self.urls.remove(cache_name)        

    def delete_all(self):
        none_cache = { url: None for url in self.urls }
        if len(none_cache.keys()) > 0:
            cache.set_many(none_cache)
        self.urls = [] # reset



bill_cache = CacheController('bill')