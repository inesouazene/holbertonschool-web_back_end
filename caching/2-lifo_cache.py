#!/usr/bin/python3
""" 2-lifo_cache.py """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache: cache system using LIFO algorithm """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if (key not in self.cache_data and
                    len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_key)
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None
        return self.cache_data.get(key)
