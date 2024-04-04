#!/usr/bin/env python3
''' Task 3: LRU Caching

This script defines a caching system using the Least Recently Used (LRU) algorithm.
It implements the LRUCache class, which inherits from BaseCaching.
'''

from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    ''' A class that implements an LRU caching system.

    Inherits from BaseCaching and manages a cache using the Least Recently Used (LRU) algorithm.
    '''

    def __init__(self):
        ''' Initializes the LRU cache.

        Initializes the cache_data dictionary as an ordered dictionary to maintain insertion order.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Adds an item to the cache using the LRU algorithm.

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.

        If key or item is None, this method does nothing.
        If the key is not already in the cache, it is added.
        If the cache is full, it removes the least recently used item (LRU) and adds the new item.
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves an item from the cache using the LRU algorithm.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item linked to the provided key, or None if the key is not found in the cache.

        Moves the accessed item to the end of the cache to maintain its recent usage.
        '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
