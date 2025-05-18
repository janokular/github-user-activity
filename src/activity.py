import http.client
import json


def fetch(username):
    '''Fetch data from GitHub REST API'''
    # Connect to GitHub API
    conn = http.client.HTTPSConnection("api.github.com")

    # Make request
    conn.request("GET", f"/users/{username}/events", headers={"User-Agent": "github_activity.py"})

    # Get response
    response = conn.getresponse().read()

    # Close connection
    conn.close()

    return response


def format_response(response):
    '''Format JSON response'''
    # Parse JSON
    activities = json.loads(response.decode("utf-8"))
    print('Output:')
    print(activities)


def display(username):
    '''Display the user's recent activity'''
    format_response(fetch(username))
