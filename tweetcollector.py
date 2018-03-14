#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy


class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(self.auth)
        print(self.api.rate_limit_status()['resources']['search'])

    def get_user_tweets(self, screen_name):
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name, tweet_mode="extended").items():
            yield {'text': tweet.full_text, 'label': ''}

    def search(self, search_query):
        for tweet in tweepy.Cursor(self.api.search, q=search_query, tweet_mode="extended").items():
            yield {'text': tweet.full_text, 'label': ''}
