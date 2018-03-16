#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import TweetTokenizer


class TwitterTokenizer:

    def __init__(self, doc_generator):
        self.doc_generator = doc_generator
        self.tweet = ''
        self.tokenizer = TweetTokenizer(reduce_len=True)

    def __iter__(self):
        for doc in self.doc_generator:
            self.tweet = doc['text']
            tokenized = self.tokenizer.tokenize(doc['text'])
            tokens = []
            for i, token in enumerate(tokenized):
                feed_dict = {'id': i, 'token': token, 'label': ''}
                tokens.append(feed_dict)

            yield tokens
