import os

SECRET_FILE_JSON = 'client_secret_381305864734-43q392id5rp0ebdh3e19k0kmk5s6h32e.apps.googleusercontent.com.json'


def get_client_secrets_file():
    return os.path.join(base_dir(), SECRET_FILE_JSON)


def base_dir():
    result = os.path.dirname(__file__)
    while result and not result.endswith('Expirements'):
        result = os.path.dirname(result)
    return result
