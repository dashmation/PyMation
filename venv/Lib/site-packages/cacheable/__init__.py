__author__ = 'dpepper'
__version__ = '0.2.2'


import types

from adapter import CacheableAdapter
from adapter import DictAdapter


class Cacheable:
    VERSION = 1
    TTL = 0
    adapter = None


    def __init__(self):
        raise Exception('use Cacheable.init()')

    @staticmethod
    def init(adapter=None):
        assert isinstance(adapter, CacheableAdapter),  \
            'expected a %s, found %s' % (CacheableAdapter.__name__, adapter)

        if not isinstance(adapter, DictAdapter):
            Cacheable.adapter = adapter


    @classmethod
    def cachekey_prefix(cls):
        return '%s:%s:' % (cls.__name__.lower(), cls.VERSION)


    @classmethod
    def cachekeys(cls, keys):
        prefix = cls.cachekey_prefix()
        cachekeys = {}

        for key in keys:
            cachekeys[key] = '%s%s' % (prefix, key)

        return cachekeys

    @classmethod
    def cachekey(cls, key):
        return cls.cachekeys([ key ]).get(key)


    @classmethod
    def multiget(cls, keys):
        cachekeys = cls.cachekeys(keys)

        if not hasattr(cls, 'cache'):
            # initialize here instead of at class level so that each
            # subclass has it's own cache, instead of the same global one
            cls.cache = DictAdapter()


        # check local cache
        missing_keys = set(keys)
        for key in list(missing_keys):
            if cls.cache.get(key):
                missing_keys.remove(key)

        # check DB cache
        if missing_keys and cls.adapter:
            kv = cls.adapter.multiget([ cachekeys[key] for key in missing_keys ])
            for key in list(missing_keys):
                if kv.has_key(cachekeys[key]):
                    cls.cache.set(key, kv[cachekeys[key]], cls.TTL)
                    missing_keys.remove(key)

        if missing_keys:
            data = cls.load_data(list(missing_keys))
            if set(data.keys()) != set(missing_keys):
                raise Exception('%s::load_data() did not return all values' % cls.__name__)

            if cls.adapter:
                cls.adapter.multiset({ cachekeys[key] : value for key, value in data.items() }, cls.TTL)

            cls.cache.multiset(data, cls.TTL)

        return cls.cache.multiget(keys)

    @classmethod
    def get(cls, key):
        return cls.multiget([ key ]).get(key)


    @classmethod
    def delete(cls, key_or_keys):
        if list == type(key_or_keys):
            keys = key_or_keys
        else:
            keys = [ key_or_keys ]

        cachekeys = cls.cachekeys(keys)

        if cls.adapter:
            cls.adapter.delete(cachekeys.values())

        if hasattr(cls, 'cache'):
            cls.cache.delete(keys)


    @classmethod
    def list(cls, limit=None):
        prefix = cls.cachekey_prefix()

        if cls.adapter:
            res = cls.adapter.list(prefix, limit)
        elif hasattr(cls, 'cache'):
            res = cls.cache.list(limit=limit)
        else:
            res = []

        return res

    @staticmethod
    def load_data(keys):
        raise NotImplementedError
