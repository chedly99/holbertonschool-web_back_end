#!/usr/bin/python3
""" 0-basic_cache.py """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """[summary]
    cashe class
    """
    def put(self, key, item):
        """[summary]
        insert data to cashe
        """
        if key is None or item is None:
            return 
        self.cache_data[key] = item
    
    def get(self, key):
        """[summary]
        value of(key)
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]