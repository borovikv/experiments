import twitter

from utils.credentials import get_tweeter_credentials

credentials = get_tweeter_credentials()


def twitter_py_lib(q='Quibi', result_type='recent', c=1, start_date='2019-01-01'):
    api = twitter.Api(**credentials)
    raw_query = f'q={q}&result_type={result_type}&since={start_date}&count={c}'
    results = api.GetSearch(raw_query=raw_query, include_entities=True)
    attrs = [a for a in dir(results[0]) if not a.startswith('_')]
    for r in results:
        for a in attrs:
            print(f'{a}: {getattr(r, a)}')

# twitter_py_lib()
