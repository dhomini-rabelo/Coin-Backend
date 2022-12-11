from rest_framework.request import HttpRequest
from django.core.cache import cache
from .typings import has_cache_response_type
from typing import Any

class CacheController:

    def __init__(self, cache_name: str):
        self._cache_name = cache_name

    @property
    def cache_name(self): return self._cache_name

    def _get(self, request: HttpRequest, id_for_cache: str | None = None) -> Any:
        print('cache -> get: ', self._get_cache_name_for_save(request.path, id_for_cache))
        return cache.get(self._get_cache_name_for_save(request.path, id_for_cache))

    def has_cache(self, request: HttpRequest, id_for_cache: str | None = None) -> has_cache_response_type:
        saved_cache = self._get(request, id_for_cache)
        print('cache -> has_cache: ', self._get_cache_name_for_save(request.path, id_for_cache), saved_cache is not  None)
        return {
            "response": saved_cache is not None,
            "cache_data": saved_cache,
        }

    def _get_cache_name_for_save(self, url: str, id_for_cache: str | None = None) -> str:
        return f'{self._cache_name}-{url}-{id_for_cache}' if id_for_cache else f'{self._cache_name}-{url}'

    def save(self, data: Any, request: HttpRequest, id_for_cache: str | None = None):
        cache_name_for_save = self._get_cache_name_for_save(request.path, id_for_cache)
        print('cache -> save: ', cache_name_for_save, data)
        cache.set(cache_name_for_save, data, None)

    def delete_only(self, url: str, cache_id: str):
        cache_name_for_delete = self._get_cache_name_for_save(url, cache_id)
        print('cache -> delete_only: ', cache_name_for_delete)
        cache.delete(cache_name_for_delete) 

    def delete_all(self):

        def clear_key(key: bytes) -> str:
            decoded_key = key.decode('ascii')
            key_without_client_number = decoded_key[(decoded_key.index(':', 1) + 1):]
            return key_without_client_number

        all_cache_keys_as_binary_string_and_with_client_number = cache._cache.get_client().keys('*')
        all_cache_keys = [clear_key(key) for key in all_cache_keys_as_binary_string_and_with_client_number]
        keys_for_delete = [key for key in all_cache_keys if key.startswith(self._cache_name)]
        cache.delete_many(keys_for_delete)



bill_cache = CacheController('bill')