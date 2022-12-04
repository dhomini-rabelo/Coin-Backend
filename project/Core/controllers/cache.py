from rest_framework.request import HttpRequest
from django.core.cache import cache
from typing import Any


class CacheController:

    def __init__(self, cache_name: str):
        self.name = cache_name
        self.urls: list[str] = []

    def get(self, request: HttpRequest, id_for_cache: str | None = None) -> Any:
        print('cache -> get', self.urls, self.get_cache_name_for_save(request.path, id_for_cache))
        return cache.get(self.get_cache_name_for_save(request.path, id_for_cache))

    def has_cache(self, request: HttpRequest, id_for_cache: str | None = None) -> bool:
        print('cache -> has_cache', self.urls, self.get_cache_name_for_save(request.path, id_for_cache))
        return self.get_cache_name_for_save(request.path, id_for_cache) in self.urls

    def get_cache_name_for_save(self, url: str, id_for_cache: str | None = None) -> str:
        return f'{self.name}-{url}-{id_for_cache}' if id_for_cache else f'{self.name}-{url}'

    def save(self, data: Any, request: HttpRequest, id_for_cache: str | None = None):
        cache_name_for_save = self.get_cache_name_for_save(request.path, id_for_cache)
        print('cache -> save', self.urls, cache_name_for_save)
        cache.set(cache_name_for_save, data, None)
        self.urls.append(cache_name_for_save)

    def delete_only(self, url: str, cache_id: str):
        cache_name_for_delete = self.get_cache_name_for_save(url, cache_id)
        print('cache -> delete_only', self.urls, cache_name_for_delete)
        if cache_name_for_delete in self.urls:
            cache.set(cache_name_for_delete, None)
            self.urls.remove(cache_name_for_delete)        

    def delete_all(self):
        print('cache -> delete_all', self.urls)
        none_cache = { url: None for url in self.urls }
        if len(none_cache.keys()) > 0:
            cache.set_many(none_cache)
        self.urls = [] # reset



bill_cache = CacheController('bill')