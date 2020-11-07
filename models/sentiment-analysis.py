# Source: https://github.com/llSourcell/twitter_sentiment_challenge
# Objective: Analyse the sentiments of tweets on Twitter
# Steps
# 1. Register for Twitter API
# 2. Install Depdendencies: tweepy, textblob
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

import tweepy
from textblob import TextBlob
import json
import csv

# Pick config keys to use
with open('configkey.json','r') as config_file:
    twit = json.load(config_file)

consumer_key = twit['consumer_key']
consumer_secret = twit['consumer_secret']

access_token = twit['access_token'] 
access_token_secret = twit['access_token_secret']

# Authenticate Twitter Login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up the Twitter API
api = tweepy.API(auth)

# Search Tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    # Polarity measures how negative or positive the sentiment is
    # Subjectivty measures how factual the data is
    # print(analysis.sentiment)
