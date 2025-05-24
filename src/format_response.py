import sys


def format(response):
    '''Format JSON response'''
    # Dictionary for counting event occurrences
    # 'event,repo': count
    activities = {}

    # Check if response is not empty
    if not bool(response):
        print('No recent events')
        sys.exit()
    
    # Count the event occurrences
    for event in response:
        event_repo_key = event['type'] + ',' + event['repo']['name']
        activities.setdefault(event_repo_key, 0)
        activities[event_repo_key] = activities[event_repo_key] + 1

    return activities
