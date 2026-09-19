# Caching

Advanced Python Programming | ALU BSE

## Description

This project implements several classic caching (cache replacement)
algorithms in Python, each as a class that inherits from a shared
`BaseCaching` parent class. A caching system is a component that stores
a limited amount of data in fast-access memory so that repeated
requests for the same data don't have to hit a slower resource (like a
database or disk) every time. Because memory is limited, once a cache
reaches capacity it must decide which existing item to remove in order
to make room for a new one — the different algorithms below are
different strategies for making that decision.

## Files

| File | Description |
|------|-------------|
| `base_caching.py` | Parent class `BaseCaching`: defines `MAX_ITEMS`, the `cache_data` dictionary, and the `put`/`get` interface every cache class must implement. |
| `0-basic_cache.py` | `BasicCache` — no limit; stores everything indefinitely. |
| `1-fifo_cache.py` | `FIFOCache` — First In, First Out: discards the item that was inserted longest ago. |
| `2-lifo_cache.py` | `LIFOCache` — Last In, First Out: discards the item that was most recently inserted. |
| `3-lru_cache.py` | `LRUCache` — Least Recently Used: discards the item that hasn't been accessed (put or get) for the longest time. |
| `4-mru_cache.py` | `MRUCache` — Most Recently Used: discards the item that was accessed (put or get) most recently. |

## Learning Objectives

- What a caching system is, and its purpose: keeping frequently or
  recently used data close at hand so future lookups are fast, instead
  of repeating an expensive fetch (e.g. a database query) every time.
- What limits a caching system has: memory is finite, so a cache can
  only hold so many items (`BaseCaching.MAX_ITEMS` here) before it must
  evict something — and every eviction policy is a trade-off, since no
  strategy is optimal for every access pattern.
- **FIFO** (First In, First Out): evicts the oldest inserted item,
  regardless of how often it's been used since.
- **LIFO** (Last In, First Out): evicts the most recently inserted
  item, like popping the top of a stack.
- **LRU** (Least Recently Used): evicts the item that has gone the
  longest without being accessed; assumes recently used data is more
  likely to be used again soon.
- **MRU** (Most Recently Used): evicts the item that was accessed most
  recently; useful in access patterns where once something's been used,
  it's unlikely to be needed again soon.
- **LFU** (Least Frequently Used, referenced in the project resources):
  evicts the item with the fewest total accesses, regardless of
  recency.

## Requirements

- Ubuntu 18.04 LTS, Python 3.7 (`python3`)
- Every file starts with `#!/usr/bin/env python3`, ends with a newline,
  and is executable
- pycodestyle (version 2.5) compliant
- Every module, class, and function has a real documentation string
