#!/usr/bin/env python3

""" FIFOCache class that inherits from BaseCaching"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assign to dictionary self.cache_data """

        if key is None or item is None:
            return
            
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discard}")

        self.cache_data[key] = item


    def get(self, key):
        """ returns item that is linked to key in cache_data"""
        return self.cache_data.get(key, None)