#!/usr/bin/python3
""" Inheriting from BaseCaching and implements Lifo"""


from base_caching import BaseCaching  # Assuming you have BaseCaching defined in base_caching.py


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching and implements LIFO caching algorithm """

    def __init__(self):
        super().__init__()  # Call parent class constructor

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the last item (LIFO algorithm)
            last_key = next(reversed(self.cache_data))  # Get the last (recently added) key
            del self.cache_data[last_key]  # Remove the last item from the cache
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """ Get an item from the cache """
        return self.cache_data.get(key, None)  # Return the item linked to the key or None if not found
