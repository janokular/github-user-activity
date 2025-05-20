import http.client
import json
import sys


def fetch(username: str):
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

    # Check if there are any recent activities
    if not len(activities):
        print('No recent events')
        sys.exit()
    
    # Format the output
    print('Output:')
    for activity in activities:
        event = activity['type']
        repo = activity['repo']['name']
        print(f'- {event} {repo}')


def display(username: str):
    '''Display the user's recent activity'''
    format_response(fetch(username))
