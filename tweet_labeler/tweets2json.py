#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from tweetcollector import TwitterAPI


def tw2js(data):
    with open('tweets.json', 'w') as outfile:
        json.dump(data, outfile)


# Twitter API
consumer_key = 'uzludXf9EsGOGfoPpL4ibe1N6'
consumer_secret = 'QABjGRsJ46N7KFPRAHyy3Fl8S8x2OnrnvkeORK4pedXRFNviv1'
access_token = '703245298932563968-LCnaCNU8qNkqoHpFabWH1LWt1Qaay9I'
access_token_secret = 'qXPH1ES9EvdwPi2JAwZAjKHENyTtoPO9swWybJi7mvp8K'

# Initializes your TwitterAPI object
tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# You can change the name (screen name) of the user.
user_tweet_generator = tw.get_user_tweets('@realDonaldTrump')

tweets = []

for tweet in user_tweet_generator:
    tweets.append(tweet)

tw2js(tweets)

''' This is an example code, it creates a tweets.json file '''
