#!/usr/bin/env python3
'''
Module for FIFO cache
'''
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """object that allows data transfer from and into a dictionary with a FIFO
    removal routine"""
    def __init__(self):
        """Initializes cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Gets an item with a key"""
        return self.cache_data.get(key, None)
