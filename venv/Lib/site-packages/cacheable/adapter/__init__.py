"""
Plumming to connect the Cacheable layer to some storage
"""

class CacheableAdapter:
    def multiget(self, keys):
        raise NotImplementedError

    def get(self, key):
        return self.multiget([ key ]).get(key)

    def multiset(self, data, ttl=None):
        raise NotImplementedError

    def set(self, key, value, ttl=None):
        self.multiset({ key : value }, ttl)

    def delete(self, keys):
        raise NotImplementedError

    def list(self, prefix=None, limit=None):
        raise NotImplementedError


from DictAdapter import DictAdapter

try:
    import peewee
    from PeeweeAdapter import PeeweeAdapter
except ImportError:
    pass
