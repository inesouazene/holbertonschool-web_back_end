#!/usr/bin/python3
""" 0-basic_cache.py """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache: simple cache with no limit """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None
        return self.cache_data.get(key)
