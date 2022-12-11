from typing import Any, TypedDict


has_cache_response_type = TypedDict('has_cache_response_type', {
    'response': bool, 'cache_data': Any
})