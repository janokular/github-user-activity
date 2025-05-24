import http.client
import json
import sys


GITHUB_API_URL = 'api.github.com'
USER_AGENT = 'github_activity.py'


def fetch(username: str):
    '''Fetch data from GitHub REST API'''
    # Connect to GitHub API
    conn = http.client.HTTPSConnection(GITHUB_API_URL)

    # Make a request
    conn.request('GET', f'/users/{username}/events', headers={'User-Agent': USER_AGENT})

    # Get a response
    response = conn.getresponse()

    # Check response status code 200 OK
    if response.status != 200:
        print('Something went wrong')
        conn.close()
        sys.exit()

    # Parse JSON
    response_body = response.read()

    # Close a connection
    conn.close()

    return json.loads(response_body.decode('utf-8'))
