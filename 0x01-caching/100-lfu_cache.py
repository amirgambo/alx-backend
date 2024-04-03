#!/usr/bin/python3
'''
LFU (Least Frequently Used) caching
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache class using LFU caching and inherits from BaseCaching
    '''

    def __init__(self):
        '''
        Initializes the class
        '''
        super().__init__()
        self.stack = []
        self.stack_count = {}

    def put(self, key, item):
        '''
        Adds item to dictionary

        Args:
            key: Key value to reference dictionary
            item: Value to be inserted in dictionary

        Return: Dictionary updated
        '''
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.stack_count.get(key, None)

        if item_count is not None:
            self.stack_count[key] += 1
        else:
            self.stack_count[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.stack.pop(0)
            del self.stack_count[to_discard]
            del self.cache_data[to_discard]
            print("DISCARD: {}".format(to_discard))

        if key not in self.stack:
            self.stack.insert(0, key)

        self.reorder_count(item=key)

    def get(self, key):
        '''
        Returns items from dictionary based on key

        Args:
            key: Key value to obtain value

        Return: Valued represented by key
        '''
        value = self.cache_data.get(key, None)
        if value is not None:
            self.stack_count[key] += 1
            self.reorder_count(item=key)

        return value

    def reorder_count(self, item):
        '''
        Assist function edits count

        Args:
            item: Value to increace count

        Return: Ammends counts less the key
        '''
        length = len(self.stack)

        idx = self.stack.index(item)
        item_count = self.stack_count[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.stack[i + 1]
                nxt_count = self.stack_count[nxt]

                if nxt_count > item_count:
                    break

        self.stack.insert(i + 1, item)
        self.stack.remove(item)
