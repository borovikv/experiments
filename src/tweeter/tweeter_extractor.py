import twitter

from utils.credentials import get_tweeter_credentials

credentials = get_tweeter_credentials()
api = twitter.Api(**credentials)

results = api.GetSearch(raw_query="q=Donald Trump&result_type=recent&since=2019-01-01&count=1", include_entities=True)

r = results[0]
for a in dir(r):
    if a.startswith('_'):
        continue
    print(f'{a}: {getattr(r, a)}')
