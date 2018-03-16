#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from tweetcollector import TwitterAPI
from tweettokenizer import TwitterTokenizer


def tw2js(data):
    with open('tweets.json', 'w') as outfile:
        json.dump(data, outfile)


# Twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Initializes your TwitterAPI object
tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# You can change the name (screen name) of the user.
user_tweet_generator = tw.get_user_tweets('@realDonaldTrump')

tokens_generator = TwitterTokenizer(user_tweet_generator)

tweets = []

for tweet in tokens_generator:
    data = {'text': tokens_generator.tweet, 'tokens': tweet}
    tweets.append(data)

tw2js(tweets)

''' This is an example code, it creates a tweets.json file '''
