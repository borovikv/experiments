import csv
import re

import twitter.extractor as extractor
from twitter.preprocessing import COLS, process_status
from utils.credentials import get_tweeter_credentials
from utils.env_utils import get_path_to_the_data_dir
import datetime

class CsvWriter:
    def __init__(self, file_name):
        self.f = open(get_path_to_the_data_dir(file_name), 'w')
        self.writer = csv.DictWriter(self.f, COLS)
        self.writer.writeheader()

    def writerows(self, rows):
        self.writer.writerows(rows)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


def csv_extractor(keywords, extract_method):
    credentials = get_tweeter_credentials()
    file_name = file_name_from_keywords(keywords)
    with CsvWriter(file_name) as writer:
        extract_method(credentials, keywords, writer=writer, preprocessor=process_status)


def file_name_from_keywords(q: str):
    name = re.sub(r'[^a-z0-9_]', '', q.lower())
    t = get_version()
    return f'{name}_{t}.csv'


def get_version():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


if __name__ == '__main__':
    # print(get_version())
    # tuesday: 12:42
    queries = [
        '#BlackLivesMatter',
        '#GeorgeFloydprotest',
        '#GeorgeFloydMurder',
        '#GeorgeFloydProtests',
        '#GeorgeFloydProtesters',
        '#crunchyroll'
    ]
    for s in queries:
        csv_extractor(s, extractor.search_latest_7_day)
    # csv_extractor('#QUIBI', extractor.stream_extractor)
    # extractor.search_latest_7_day(get_tweeter_credentials(), '#QUIBI', max_results=10, total=10)
