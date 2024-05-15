import uuid
import redis
from typing import Union


class Cache:
    """
    A class for storing and retrieving data from Redis using UUIDs as keys.

    Attributes:
        self._redis (redis.Redis): A Redis client instance.

    Methods:
        __init__(): Initialize a Redis client instance and clear the database.
        store(data): Store the data in Redis with a UUID key and
        return the key.
    """

    def __init__(self):
        """A method to store an instance of the Redis client as a private
        variable named _redis (using redis.Redis()) and flush the
        instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method that stores the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
