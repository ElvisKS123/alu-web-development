#!/usr/bin/env python3
"""Defines LRUCache, a caching system using the LRU removal policy."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A caching system limited to BaseCaching.MAX_ITEMS.

    When the cache is full, the Least Recently Used item is the one
    discarded to make room for the new item. Both put and get count
    as "using" a key.
    """

    def __init__(self):
        """Initialize the cache and the list tracking usage order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache, applying the LRU policy if full.

        If either key or item is None, the cache is left unchanged.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """Return the value cached under key, marking it recently used.

        If key is None or key is not present in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
