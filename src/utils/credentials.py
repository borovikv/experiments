import json
import os

from utils.env_utils import base_dir

YOUTUBE_SECRET_FILE_JSON = 'client_secret_381305864734-43q392id5rp0ebdh3e19k0kmk5s6h32e.apps.googleusercontent.com.json'


def get_client_secrets_file():
    return os.path.join(base_dir(), YOUTUBE_SECRET_FILE_JSON)


def get_tweeter_credentials():
    path = os.path.join(base_dir(), 'credentials/tweeter_credentials.json')
    with open(path) as f:
        s = f.read()
        credentials = json.loads(s)
    credentials_file_keys = ['consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret']
    twython_keys = ['app_key', 'app_secret', 'oauth_token', 'oauth_token_secret']
    return {tk: credentials[ck] for tk, ck in zip(twython_keys, credentials_file_keys)}
