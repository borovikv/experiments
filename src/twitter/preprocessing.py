import re

from textblob import TextBlob

from utils.nlp_utils.word_categories import get_stop_words

# columns of the csv file
COLS = ['id', 'created_at', 'source', 'clean_text', 'polarity', 'subjectivity', 'lang',
        'favorite_count', 'retweet_count', 'original_author', 'possibly_sensitive', 'hashtags',
        'user_mentions', 'place', 'place_coord_boundaries']


def process_status(status):
    filtered_tweet = clean_text(status['text'])
    blob = TextBlob(filtered_tweet)
    return {
        'id': status['id'],
        'created_at': status['created_at'],
        'source': status['source'],
        'clean_text': filtered_tweet,
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity,
        'lang': status['lang'],
        'favorite_count': status['favorite_count'],
        'retweet_count': status['retweet_count'],
        'original_author': status['user']['screen_name'],
        'possibly_sensitive': status.get('possibly_sensitive'),
        'hashtags': get_hashtags(status),
        'user_mentions': get_user_mentions(status),
        'place': get_coordinates(status),
        'place_coord_boundaries': get_location(status),
    }


def clean_text(tweet: str):
    words = re.split(r'[^a-z0-9_]', tweet.lower())
    return ' '.join([w for w in words if len(w) > 1 and w not in get_stop_words()])


def get_hashtags(status):
    return ", ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])


def get_user_mentions(status):
    return ", ".join([mention['screen_name'] for mention in status['entities']['user_mentions']])


def get_coordinates(status):
    try:
        return [coord for loc in status['place']['bounding_box']['coordinates'] for coord in loc]
    except TypeError:
        return None


def get_location(status):
    try:
        return status['user']['location']
    except TypeError:
        return ''
