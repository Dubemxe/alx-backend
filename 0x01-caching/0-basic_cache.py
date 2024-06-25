#!/usr/bin/env python3
'''
Module for Basic Cache
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """object that allows data transfer from and into a dictionary"""
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item with a key"""
        return self.cache_data.get(key, None)
