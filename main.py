#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoutils import *
from tweetcollector import TwitterAPI
from tweettokenizer import TwitterTokenizer


# Twitter API
# You should sign in to twitter developers to get these
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Mongodb Client.
# These are the names of your database (mongodb) and its collection.
db_name = 'Twitter'
collection_name= 'Tweets'

# Initializes your TwitterAPI object
tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# You can change the name (screen name) of the user.
user_tweet_generator = tw.get_user_tweets('@realDonaldTrump')

# You can even retrieve search query results, you can change the query below as you like.
search_query_tweet_generator = tw.search('#CrazySummer')

# This is a helper function to tokenize tweets using nltk's twitter tokenizer.
tokenized_tweet_generator = TwitterTokenizer(user_tweet_generator)

# You can write your tweets to mongodb like below.
mdb_writer = MongodbWriter(iter(user_tweet_generator), db_name, collection_name)
# Or you can fetch data using the function below
mdb_reader = MongodbReader(db_name, collection_name)

''' These methods are all generators. You can Iterate over them using for(-each) loops'''
