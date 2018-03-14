#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo


class MongodbClient:
    def __init__(self, database_name, collection_name, uri=None):
        self.mongo_client = pymongo.MongoClient(uri)
        self.db = self.mongo_client[database_name]
        self.collection = self.db[collection_name]


class MongodbWriter(MongodbClient):
    def __init__(self, tweets_generator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tweets_generator = tweets_generator

    def __iter__(self):
        for tweet in self.tweets_generator:
            yield self.collection.insert_one(tweet)


class MongodbReader(MongodbClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for doc in self.collection.find():
            yield doc
