#!/usr/bin/env python3
"""Defines FIFOCache, a caching system using the FIFO removal policy."""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system limited to BaseCaching.MAX_ITEMS.

    When the cache is full, the item that was inserted first (First In,
    First Out) is the one discarded to make room for the new item.
    """

    def __init__(self):
        """Initialize the cache and the list tracking insertion order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache, applying the FIFO policy if full.

        If either key or item is None, the cache is left unchanged.
        Re-putting an existing key updates its value without changing
        its position in the insertion order.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Return the value cached under key.

        If key is None or key is not present in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
