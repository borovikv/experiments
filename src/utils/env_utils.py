import os


def base_dir():
    result = os.path.dirname(__file__)
    while result and not result.lower().endswith('experiments'):
        result = os.path.dirname(result)
    return result


def get_path_to_the_data_dir(name):
    return os.path.join(base_dir(), 'data', name)
