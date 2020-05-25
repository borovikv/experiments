import os


def base_dir():
    result = os.path.dirname(__file__)
    while result and not result.endswith('Expirements'):
        result = os.path.dirname(result)
    return result


def in_project_path(*args):
    return os.path.join(base_dir(), *args)
