from twython import Twython, TwythonStreamer

from utils.credentials import get_tweeter_credentials

credentials = get_tweeter_credentials()


def search_latest_7_day(q='"data science"'):
    t = Twython(credentials['consumer_key'], credentials['consumer_secret'])
    search = t.search(q=q)  # recent 1 week
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
    for status in search['statuses']:
        user = status['user']['screen_name']
        text = status['text']
        print(f'{user}: {text}\n')


# search_latest_7_day()

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


stream = TStreamer(
    credentials['consumer_key'],
    credentials['consumer_secret'],
    credentials['access_token_key'],
    credentials['access_token_secret']
)
stream.statuses.filter(track='data')
print(stream.tweets)
# If all public
# stream.statuses.sample()
