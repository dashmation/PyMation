from time import time

from . import CacheableAdapter


class DictAdapter(CacheableAdapter):
    def __init__(self):
        self.data = {}

    def multiget(self, keys):
        ts = time()

        res = {}
        for k, v in self.data.items():
            if k in keys:
                if not v[1] or v[1] > ts:
                    res[k] = v[0]

        return res


    def multiset(self, data, ttl=None):
        if ttl:
            xts = int(time() + ttl)
        else:
            xts = 0

        data = { k : (v, xts) for k, v in data.items() }

        self.data.update(data)


    def delete(self, keys):
        for key in keys:
            if self.data.has_key(key):
                del self.data[key]


    def list(self, prefix=None, limit=None):
        ts = time()

        res = {}
        for k, v in self.data.items():
            if not prefix or k.startswith(prefix):
                if not v[1] or v[1] > ts:
                    res[k] = v[0]

        if limit:
            res = res[:limit]

        return res
