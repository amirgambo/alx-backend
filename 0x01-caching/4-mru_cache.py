#!/usr/bin/python3
'''
MRU (Most Recently Used) caching
'''


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache class using MRU caching and inherits from BaseCaching
    '''

    def __init__(self):
        '''
        Initializes the class
        '''
        super().__init__()
        self.stack = []

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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.stack.pop()
            del self.cache_data[to_discard]
            print("DISCARD: {}".format(to_discard))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.reorder(key=key)

    def get(self, key):
        '''
        Returns items from dictionary based on key

        Args:
            key: Key value to obtain value

        Return: Valued represented by key
        '''
        value = self.cache_data.get(key, None)
        if value is not None:
            self.reorder(key=key)
        return value

    def reorder(self, key):
        '''
        Assist function to move elements to end of list

        Args:
            key: Key to determine value to move

        Return: Reorder List
        '''
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
