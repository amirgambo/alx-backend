#!/usr/bin/env python3
'''
Basic caching creates a dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Creates a dictionary using class BasicCache which inherits from
    BaseCaching
    '''

    def put(self, key, item):
        '''
        Adds item to dictionary

        Args:
            key: Key value to reference dictionary
            item: Value to be inserted in dictionary

        Return: Dictionary updated
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Returns items from dictionary based on key

        Args:
            key: Key value to obtain value

        Return: Valued represented by key
        '''

        return self.cache_data.get(key, None)
