#!/usr/bin/env python3
'''
Module for LIFO Cache
'''
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """object that allows items transfer to and from a dictionary
    with a LIFO removal technic"""
    def __init__(self):
        """Initializes cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item to the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets an item with a key"""
        return self.cache_data.get(key, None)
