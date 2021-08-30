import logging
import pickle

from redis import StrictRedis

redis = StrictRedis(host='redis', port=6379)


def save_cache(key, value):
    if data := redis.hset('cities', key, pickle.dumps(value)):
        return data


def get_from_cache(key):
    if data := redis.hget('cities', key):
        return pickle.loads(data)
