#!/usr/bin/env python3
"""Defines BasicCache, a caching system with no item limit."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from BaseCaching and has no limit.

    Every key/value pair put into the cache stays there forever - there
    is no maximum number of items and nothing is ever discarded.
    """

    def put(self, key, item):
        """Add an item to the cache under the given key.

        If either key or item is None, the cache is left unchanged.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value cached under key.

        If key is None or key is not present in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
