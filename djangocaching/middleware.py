import re

from django.conf import settings
from django.core.cache import cache

CACHE_URLS = [(re.compile(url), cache_time)
              for (url, cache_time) in settings.CACHE_URLS]


class CachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        path = request.path_info.lstrip('/')
        url_should_be_cached = any(url.match(path)
                                   for (url, time) in CACHE_URLS)

        for (url, time) in CACHE_URLS:
            if url.match(path):
                url_should_be_cached = True
                cache_time = time

        if url_should_be_cached:
            cached_page = cache.get(path)
            if cached_page is None:
                cache.set(path, response, cache_time)
                return response
            else:
                return cache.get(path)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass
