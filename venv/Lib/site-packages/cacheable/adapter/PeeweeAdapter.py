import peewee
import playhouse.kv
from time import time

from . import CacheableAdapter


class PeeweeAdapter(CacheableAdapter, peewee.Model):
    key = peewee.CharField(max_length=256, unique=True)
    value = playhouse.kv.JSONField()
    mtime = peewee.IntegerField(default=time)
    ttl = peewee.IntegerField(default=0)

    class Meta:
        database = peewee.Proxy()


    def __init__(self, db_connection, table_name=None):
        if table_name:
            self._meta.db_table = table_name

        self._meta.database.initialize(db_connection)


    def multiget(self, keys):
        cls = self.__class__
        res = self.select(cls.key, cls.value)  \
            .where(cls.key << keys & self.__ttl_filter())  \
            .tuples()

        return { x[0] : x[1] for x in res }

    @classmethod
    def multiset(cls, data, ttl=None):
        ts = int(time())
        ttl = ttl or 0
        kvs = []
        for key, value in data.items():
             kvs.append({
                cls.key : key,
                cls.value : value,
                cls.mtime : ts,
                cls.ttl : ttl,
            })
        cls.insert_many(kvs).upsert().execute()


    def delete(self, key_or_keys):
        if list == type(key_or_keys):
            keys = key_or_keys
        else:
            keys = [ key_or_keys ]

        cls = self.__class__
        peewee.DeleteQuery(cls).where(cls.key << keys).execute()


    def list(self, prefix=None, limit=None):
        cls = self.__class__

        q = self.select(cls.key, cls.value)

        if prefix:
            if self.__db_type() == peewee.SqliteDatabase:
                wildcard = '*'
            else:
                wildcard = '%'

            q = q.where(cls.key % ('%s%s' % (prefix, wildcard)))

        q = q.where(self.__ttl_filter())

        if limit:
            q = q.limit(limit)

        res = { x[0] : x[1] for x in q.tuples() }

        if prefix:
            res = { k[len(prefix):] : v for k, v in res.items() }

        return res


    def __ttl_filter(self):
        """
        Add the TTL where clause to a query, to filter out stale results
        """
        ts = int(time())

        cls = self.__class__
        return cls.ttl == 0 | (cls.mtime + cls.ttl > ts)


    def __db_type(self):
        return type(self._meta.database.obj)
