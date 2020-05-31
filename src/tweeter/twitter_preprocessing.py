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
import os

from utils.credentials import get_tweeter_credentials
from utils.env_utils import base_dir

credentials = get_tweeter_credentials()

#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token_key'], credentials['access_token_secret'])
api = tweepy.API(auth)

#declare file paths as follows for three files
telemedicine_tweets = os.path.join(base_dir(),"data/telemedicine_data.csv")
epilepsy_tweets = os.path.join(base_dir(),"data/epilepsy_data.csv")
heart_stroke_tweets = os.path.join(base_dir(),"data/heart_stroke_tweets_data.csv")

#columns of the csv file
COLS = ['id', 'created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang',
'favorite_count', 'retweet_count', 'original_author',   'possibly_sensitive', 'hashtags',
'user_mentions', 'place', 'place_coord_boundaries']

#HappyEmoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])

#Emoji patterns
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)

#combine sad and happy emoticons
emoticons = emoticons_happy.union(emoticons_sad)


def clean_tweets(tweet):

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)

    # after tweepy preprocessing the colon symbol left remain after
    # #removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    # replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+', ' ', tweet)

    # remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)

    # filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []

    # looping through conditions
    for w in word_tokens:
        # check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)
    # print(word_tokens)
    # print(filtered_sentence)return tweet


def write_tweets(keyword, file):
    #If the file exists, then read the existing data from the CSV file.
    if os.path.exists(file):
        df = pd.read_csv(file, header=0)
    else:
        df = pd.DataFrame(columns=COLS)
    #page attribute in tweepy.cursor and iteration
    for page in tweepy.Cursor(api.search, q=keyword, count=200, include_rts=False):
        for status in page:
            new_entry = []
            status = status._json
            
            if status['lang'] != 'en':
                continue

            if status['created_at'] in df['created_at'].values:
                i = df.loc[df['created_at'] == status['created_at']].index[0]
                if status['favorite_count'] != df.at[i, 'favorite_count'] or \
                        status['retweet_count'] != df.at[i, 'retweet_count']:
                    df.at[i, 'favorite_count'] = status['favorite_count']
                    df.at[i, 'retweet_count'] = status['retweet_count']
                    continue

            clean_text = p.clean(status['text'])

            filtered_tweet = clean_tweets(clean_text)

            blob = TextBlob(filtered_tweet)
            Sentiment = blob.sentiment
            polarity = Sentiment.polarity
            subjectivity = Sentiment.subjectivity

            new_entry += [status['id'], status['created_at'],
                          status['source'], status['text'], filtered_tweet, Sentiment, polarity, subjectivity,
                          status['lang'],
                          status['favorite_count'], status['retweet_count'], status['user']['screen_name'], status.get('possibly_sensitive')]

            hashtags = ", ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])
            new_entry.append(hashtags) #append the hashtags
            mentions = ", ".join([mention['screen_name'] for mention in status['entities']['user_mentions']])
            new_entry.append(mentions) #append the user mentions

            try:
                coordinates = [coord for loc in status['place']['bounding_box']['coordinates'] for coord in loc]
            except TypeError:
                coordinates = None
            new_entry.append(coordinates)

            try:
                location = status['user']['location']
            except TypeError:
                location = ''
            new_entry.append(location)

            single_tweet_df = pd.DataFrame([new_entry], columns=COLS)
            df_final = df.append(single_tweet_df, ignore_index=True)

            csvFile = open(file, 'a', encoding='utf-8')
            df.to_csv(csvFile, mode='a', columns=COLS, index=False, encoding="utf-8")

telemedicine_keywords = '#telemedicine OR #telehealth OR   #digitalhealth OR #ehealth OR #digitalpatient OR #digitaltransformation'
Epilepsy_keywords = '#Epilepsy OR #epilepsyawareness OR #epilepsyaction OR #epilepsyalerts OR #epilepsybed OR #epilepsycongres OR #epilepsysurgery OR #epilepsysurgery OR #Epilepsytreatment OR #seizures OR #seizurefree'
HeartDisease_keywords = '#HeartDisease OR #stroke OR #Stroking OR #strokepatient OR #StrokeSurvivor OR #hearthealth OR #Stroke OR #HeartFailure'

write_tweets(telemedicine_keywords, telemedicine_tweets)
write_tweets(Epilepsy_keywords, epilepsy_tweets)
write_tweets(HeartDisease_keywords, heart_stroke_tweets)