import re
import time
from pprint import pprint

from twython import Twython, TwythonStreamer

from utils.credentials import get_tweeter_credentials

MAX_ID_PATTERN = re.compile(r'max_id=(?P<max_id>\d+)&')


def search_latest_7_day(credentials, q, writer=None, preprocessor=None, max_results=500, total=None):
    preprocessor = preprocessor or default_preprocessor
    tweets = (preprocessor(e) for result in search_generator(credentials, q, max_results, total) for e in result)
    if writer:
        writer.writerows(tweets)
    else:
        pprint(list(tweets))


def default_preprocessor(tweet):
    return tweet


def search_generator(credentials, q, max_results=500, total=None):
    t = Twython(**credentials)
    search = dict()
    collected = 0
    error_time = 0
    while (total is None or collected < total) and error_time < 5:
        try:
            max_id = get_max_id(search.get('search_metadata'))
            search = t.search(q=q, max_id=max_id, count=max_results, lang='en')
        except Exception as e:
            error_time += 1
            print(q, e)
            time.sleep(60 * 16)  # wait 16 min.
            # From the doc: There are two initial buckets available for GET requests:
            # 15 calls every 15 minutes, and 180 calls every 15 minutes.
            t = Twython(**credentials)
            continue
        yield search['statuses']
        collected += len(search['statuses'])
        if not search['search_metadata'].get('next_results'):
            return


def get_max_id(search_metadata):
    if not search_metadata:
        return
    next_results = search_metadata.get('next_results')
    if not next_results:
        return
    return MAX_ID_PATTERN.search(next_results)['max_id']


class RealTimeTwStreamConsumer(TwythonStreamer):
    """
    example of usage:
        with RealTimeTwStreamConsumer(writer, process_status, **credentials) as stream:
            stream.statuses.filter(track='#Quibi', since="2020-01-01")
            or
            stream.statuses.sample()
    """
    BUFFER_SIZE = 10e5

    def __init__(self, writer, preprocessor, credentials):
        super(RealTimeTwStreamConsumer, self).__init__(**credentials)
        self.tweets = []
        self.writer = writer
        self.preprocessor = preprocessor or default_preprocessor

    def on_success(self, data):
        if data['lang'] == 'en':
            self.tweets.append(self.preprocessor(data))

        if self.writer and len(self.tweets) >= RealTimeTwStreamConsumer.BUFFER_SIZE:
            self.writer.writerows(self.tweets)
            self.tweets = []

    def on_error(self, status_code, data, headers=None):
        self.disconnect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()


def stream_extractor(credentials, keywords, writer, preprocessor):
    with RealTimeTwStreamConsumer(writer, preprocessor, credentials) as stream:
        stream.statuses.filter(track=keywords)


if __name__ == '__main__':
    # search_latest_7_day('#Quibi', save_to='out.json')
    search_latest_7_day(get_tweeter_credentials(), '#Quibi', max_results=5, total=5)
