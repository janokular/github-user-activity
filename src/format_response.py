def format(response: list):
    '''
    Format the response by counting events inside each repository\n
    and return it as a dictionary {'event,repo': count}
    '''
    activities = {}
    
    for event in response:
        event_repo_key = event['type'] + ',' + event['repo']['name']
        activities.setdefault(event_repo_key, 0)
        activities[event_repo_key] = activities[event_repo_key] + 1

    return activities
