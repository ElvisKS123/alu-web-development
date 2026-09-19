#!/usr/bin/env python3
"""Defines LIFOCache, a caching system using the LIFO removal policy."""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A caching system limited to BaseCaching.MAX_ITEMS.

    When the cache is full, the most recently put item (Last In, First
    Out) - excluding the item that triggered the overflow - is the one
    discarded to make room for the new item.
    """

    def __init__(self):
        """Initialize the cache and the list tracking put order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache, applying the LIFO policy if full.

        If either key or item is None, the cache is left unchanged.
        Re-putting an existing key moves it to the top of the stack,
        since it counts as the most recent put.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order[-2]
            self.order.remove(discard_key)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Return the value cached under key.

        If key is None or key is not present in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
