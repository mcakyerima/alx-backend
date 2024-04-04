#!/usr/bin/env python3
""" Task 5: Least Frequently Used (LFU) Caching.

This script defines a caching system using the Least Frequently Used (LFU) algorithm.
It implements the LFUCache class, which inherits from BaseCaching.
"""

from collections import OrderedDict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ A class that implements an LFU caching system.

    Inherits from BaseCaching and manages a cache using the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        """ Initializes the LFU cache.

        Initializes the cache_data dictionary as an ordered dictionary to maintain insertion order.
        Initializes the keys_frequency list to track the frequency of keys accessed.
        """
        super().__init__()
        self.cache_data = OrderedDict()  # Dictionary to store cached items
        self.keys_frequency = []  # List to track key access frequency

    def __reorder_items(self, most_recently_used_key):
        """ Reorders the items in the cache based on the most recently used item.

        Args:
            most_recently_used_key: The key of the most recently used item.

        Finds the position to insert the MRU key based on its frequency of access.
        """
        positions_with_max_frequency = []
        most_recent_freq = 0
        most_recent_pos = 0
        insertion_pos = 0

        # Iterate over keys and their frequencies to find MRU key's frequency and position
        for i, key_freq_pair in enumerate(self.keys_frequency):
            key, freq = key_freq_pair
            if key == most_recently_used_key:
                most_recent_freq = freq + 1
                most_recent_pos = i
                break
            elif not positions_with_max_frequency:
                positions_with_max_frequency.append(i)
            elif freq < self.keys_frequency[positions_with_max_frequency[-1]][1]:
                positions_with_max_frequency.append(i)

        # Reverse positions list to start from highest frequency
        positions_with_max_frequency.reverse()

        # Find insertion position based on frequencies
        for pos in positions_with_max_frequency:
            if self.keys_frequency[pos][1] > most_recent_freq:
                break
            insertion_pos = pos

        # Remove MRU key from its current position and insert at the calculated position
        self.keys_frequency.pop(most_recent_pos)
        self.keys_frequency.insert(insertion_pos, [most_recently_used_key, most_recent_freq])

    def put(self, key, item):
        """ Adds an item to the cache using the LFU algorithm.

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.

        If key or item is None, this method does nothing.
        If the key is not already in the cache, it is added.
        If the cache is full, it removes the least frequently used item (LFU) and adds the new item.
        """
        if key is None or item is None:
            return

        # If key not in cache, add it; else, update frequency and reorder items
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                least_frequent_key, _ = self.keys_frequency[-1]
                self.cache_data.pop(least_frequent_key)
                self.keys_frequency.pop()
                print("DISCARD:", least_frequent_key)
            self.cache_data[key] = item
            insertion_index = len(self.keys_frequency)
            for i, key_freq_pair in enumerate(self.keys_frequency):
                if key_freq_pair[1] == 0:
                    insertion_index = i
                    break
            self.keys_frequency.insert(insertion_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """ Retrieves an item from the cache using the LFU algorithm.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item linked to the provided key, or None if the key is not found in the cache.

        Moves the accessed item to the front of the cache's frequency tracking list.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
