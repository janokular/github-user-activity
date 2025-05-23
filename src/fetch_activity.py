import http.client
import json
import sys
import re


def fetch(username: str):
    '''Fetch data from GitHub REST API'''
    # Check username before API call
    # GitHub usernames can alphanumeric characters and dashes 
    if not bool(re.search('^[a-zA-Z0-9-]*$', username)):
        print('Invalid GitHub username')
        sys.exit()

    # Connect to GitHub API
    conn = http.client.HTTPSConnection('api.github.com')

    # Make a request
    conn.request('GET', f'/users/{username}/events', headers={'User-Agent': 'github_activity.py'})

    # Get a response
    response = conn.getresponse()

    # Check response status code 200 OK
    if response.status != 200:
        print('Something went wrong')
        conn.close()
        sys.exit()

    # Parse JSON
    response_body = response.read()
    activities = json.loads(response_body.decode('utf-8'))

    # Close a connection
    conn.close()

    # Check if there are any recent activities
    if not bool(activities):
        print('No recent events')
        sys.exit()

    # Dictionary for counting event occurrences
    # 'event,repo': count
    count_events = {}
    
    # Count the event occurrences
    for event in activities:
        event_repo_key = event['type'] + ',' + event['repo']['name']
        count_events.setdefault(event_repo_key, 0)
        count_events[event_repo_key] = count_events[event_repo_key] + 1

    # Print the output
    print('Output:')
    for event_repo_key, count in count_events.items():
        # Split the keys separeted with ','
        # keys = ['event', 'repo']
        keys = event_repo_key.split(',')
        match keys[0]:
            case 'CommitCommentEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'CreateEvent':
                if count == 1:
                    print(f'- Created {count} event in {keys[1]}')
                else:
                    print(f'- Created {count} events in {keys[1]}')
            case 'DeleteEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'ForkEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'GollumEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'IssueCommentEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'IssuesEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'MemberEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PublicEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewCommentEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewThreadEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PushEvent':
                if count == 1:
                    print(f'- Pushed {count} commit into {keys[1]}')
                else:
                    print(f'- Pushed {count} commits into {keys[1]}')
            case 'ReleaseEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'SponsorshipEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'WatchEvent':
                print(f'- (!) {keys[0]} {count} {keys[1]}')
            case _:
                print(f'- Unsupported Event')
