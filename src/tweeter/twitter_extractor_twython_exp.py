import json
import re
from time import time

from twython import Twython, TwythonStreamer

from utils.credentials import get_tweeter_credentials

p = re.compile(r'max_id=(?P<max_id>\d+)&')

credentials = get_tweeter_credentials()


# dict_keys(['statuses', 'search_metadata'])
# print(search['search_metadata'])
# {
# 'completed_in': 0.083,
# 'max_id': 1261552126016266250,
# 'max_id_str': '1261552126016266250',
# 'next_results': '?max_id=1261549058222505984&q=%22data%20science%22&include_entities=1',
# 'query': '%22data+science%22',
# 'refresh_url': '?since_id=1261552126016266250&q=%22data%20science%22&include_entities=1',
# 'count': 15,
# 'since_id': 0,
# 'since_id_str': '0'
# }
def search_latest_7_day(q='"data science"'):
    s = time()
    result = list(search_generator(q))
    print(time() - s)
    result = sum(result, [])
    with open('out_1.txt', 'w') as f:
        for r in result:
            f.write(json.dumps(r) + '\n')


def search_generator(q):
    t = Twython(credentials['consumer_key'], credentials['consumer_secret'])
    max_results = 500
    search = t.search(q=q, count=max_results)  # recent 1 week
    yield search['statuses']
    i = 0
    next_results = search['search_metadata'].get('next_results')
    while next_results:
        i += 1
        print(i)
        try:
            search = t.search(q=q, max_id=get_max_id(next_results), count=max_results)  # recent 1 week
        except:
            t = Twython(credentials['consumer_key'], credentials['consumer_secret'])
            print(f'reconnect on {i}')
            continue
        yield search['statuses']
        next_results = search['search_metadata'].get('next_results')


def get_max_id(r):
    return p.search(r)['max_id']


search_latest_7_day('#Quibi')


class TStreamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        super(TStreamer, self).__init__(*args, **kwargs)
        self.tweets = []

    def on_success(self, data):
        if data['lang'] == 'en':
            self.tweets.append(data)
            print(f'received tweet #{len(self.tweets)}')

        if len(self.tweets) >= 10:
            self.disconnect()

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.disconnect()

# stream = TStreamer(
#     credentials['consumer_key'],
#     credentials['consumer_secret'],
#     credentials['access_token_key'],
#     credentials['access_token_secret']
# )
# stream.statuses.filter(track='#Quibi', since="2020-01-01")
# print(stream.tweets)
# If all public
# stream.statuses.sample()
