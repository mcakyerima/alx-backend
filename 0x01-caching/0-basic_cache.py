#!/usr/bin/python3
""" BaseCaching module """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and defines put and get methods"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        # If key or item is None, do nothing
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        # If key is None or self.cache_data has no item for key, return None
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
