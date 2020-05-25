import json
import re
import time
from pprint import pprint

from twython import Twython, TwythonStreamer

from utils.credentials import get_tweeter_credentials

MAX_ID_PATTERN = re.compile(r'max_id=(?P<max_id>\d+)&')

CREDENTIALS = get_tweeter_credentials()


def search_latest_7_day(q, save_to=None, max_results=500, total=None):
    all_results = (e for result in search_generator(q, max_results, total) for e in result)
    if save_to:
        write_to_file(all_results, save_to)
    else:
        pprint(list(all_results))


def write_to_file(rows, save_to):
    with open(save_to, 'w') as f:
        for r in rows:
            f.write(json.dumps(r) + '\n')


def search_generator(q, max_results=500, total=None):
    t = Twython(CREDENTIALS['consumer_key'], CREDENTIALS['consumer_secret'])
    search = dict()
    collected = 0
    error_time = 0
    while (total is None or collected < total) and error_time < 5:
        try:
            max_id = get_max_id(search.get('search_metadata'))
            search = t.search(q=q, max_id=max_id, count=max_results)
        except Exception as e:
            error_time += 1
            print(e)
            time.sleep(30 * error_time)
            t = Twython(CREDENTIALS['consumer_key'], CREDENTIALS['consumer_secret'])
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


if __name__ == '__main__':
    # search_latest_7_day('#Quibi', save_to='out.json')
    search_latest_7_day('#Quibi', max_results=5, total=5)
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
