import tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression
from textblob import TextBlob
import string
import preprocessor as p

from utils.credentials import get_tweeter_credentials

credentials = get_tweeter_credentials()

#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token_key'], credentials['access_token_secret'])
api = tweepy.API(auth)

