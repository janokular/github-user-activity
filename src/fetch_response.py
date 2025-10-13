import http.client
import json
import sys


GITHUB_API_URL = 'api.github.com'
USER_AGENT = 'github_activity.py'


def fetch(username: str):
    '''Fetch data from the GitHub REST API and return it as a list'''
    conn = http.client.HTTPSConnection(GITHUB_API_URL)

    conn.request('GET', f'/users/{username}/events', headers={'User-Agent': USER_AGENT})

    response_http = conn.getresponse()

    if not response_http.status == 200:
        print('error: Something went wrong')
        conn.close()
        sys.exit()

    response_body = response_http.read()

    conn.close()

    response = json.loads(response_body.decode('utf-8'))

    if not response:
        print('No recent events, response is empty')
        sys.exit()

    return response
