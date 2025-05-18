import http.client
import json


def fetch(username):
    '''Fetch data from GitHub REST API in JSON format'''
    # Connect to GitHub API
    conn = http.client.HTTPSConnection("api.github.com")

    # Make request
    conn.request("GET", f"/users/{username}/events", headers={"User-Agent": "github_activity.py"})

    # Get response
    response = conn.getresponse().read()

    # Parse JSON
    activities = json.loads(response.decode("utf-8"))

    # Close connection
    conn.close()

    return activities


def format_response(response):
    '''Format JSON response'''
    print(response)


def display(username):
    '''Display the user's recent activity'''
    response = fetch(username)
    return format_response(response)
