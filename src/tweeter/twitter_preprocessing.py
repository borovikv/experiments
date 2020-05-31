import re
import string

import tweepy
from textblob import TextBlob

from utils.collection_utils import write_to_csv
from utils.credentials import get_tweeter_credentials
from utils.env_utils import get_path_to_the_data_dir
from utils.nlp_utils.word_categories import emoji_pattern, emoticons, get_stop_words, word_tokenize


def get_tweeter_api():
    credentials = get_tweeter_credentials()
    # pass twitter credentials to tweepy
    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token_key'], credentials['access_token_secret'])
    return tweepy.API(auth)


# columns of the csv file
COLS = ['id', 'created_at', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang',
        'favorite_count', 'retweet_count', 'original_author', 'possibly_sensitive', 'hashtags',
        'user_mentions', 'place', 'place_coord_boundaries']


def collect_tweets(api, keyword, file):
    # If the file exists, then read the existing data from the CSV file.
    result = []
    for page in tweepy.Cursor(api.search, q=keyword, count=200, include_rts=False):
        for status in page:
            status = status._json
            if status['lang'] != 'en':
                continue
            result.append(process_status(status))

    write_to_csv([COLS] + result, get_path_to_the_data_dir(file))


def process_status(status):
    filtered_tweet = clean_tweets(status['text'])
    blob = TextBlob(filtered_tweet)
    new_entry = [
        status['id'], status['created_at'], status['source'], status['text'],
        filtered_tweet, blob.sentiment, blob.sentiment.polarity, blob.sentiment.subjectivity, status['lang'],
        status['favorite_count'], status['retweet_count'], status['user']['screen_name'],
        status.get('possibly_sensitive')
    ]
    hashtags = ", ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])
    new_entry.append(hashtags)  # append the hashtags
    mentions = ", ".join([mention['screen_name'] for mention in status['entities']['user_mentions']])
    new_entry.append(mentions)  # append the user mentions
    coordinates = get_coordinates(status)
    new_entry.append(coordinates)
    location = get_location(status)
    new_entry.append(location)
    return new_entry


def clean_tweets(tweet: str):
    # after tweepy preprocessing the colon symbol left remain after
    # #removing mentions
    for emoticon in emoticons:
        tweet = tweet.replace(emoticon, '')
    for p in string.punctuation:
        tweet = tweet.replace(p, '')
    tweet = re.sub(r'(:|Ä¶)', '', tweet)
    # replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+', ' ', tweet)
    # remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)
    word_tokens = word_tokenize(tweet)
    filtered_tweet = [w for w in word_tokens if not w in get_stop_words()]
    return ' '.join(filtered_tweet)


def get_location(status):
    try:
        location = status['user']['location']
    except TypeError:
        location = ''
    return location


def get_coordinates(status):
    try:
        coordinates = [coord for loc in status['place']['bounding_box']['coordinates'] for coord in loc]
    except TypeError:
        coordinates = None
    return coordinates


if __name__ == '__main__':
    telemedicine_keywords = '#telemedicine OR #telehealth OR   #digitalhealth OR #ehealth OR #digitalpatient OR #digitaltransformation'
    api = get_tweeter_api()
    collect_tweets(api, telemedicine_keywords, 'telemedicine_tweets.csv')
