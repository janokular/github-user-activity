import requests


def fetch(username: str):
    '''Fetch data from GitHub REST API'''
    response = requests.get('https://api.github.com/users/{}/events'.format(username))
    print(response)
