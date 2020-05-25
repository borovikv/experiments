import json
from pprint import pprint

from utils.env_utils import in_project_path


def parse(file_name):
    with open(in_project_path((file_name))) as f:
        for line in f:
            pprint(json.loads(line))
            break


parse('src/tweeter/out_1.txt')
