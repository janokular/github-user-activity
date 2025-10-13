def format(response: list):
    '''
    Format the response by counting events inside each repository\n
    and return it as a dictionary {'event_type,repo,action': count}
    '''
    activities = {}
    
    for event in response:
        type = event['type']
        repo = event['repo']['name']
        action = ''

        try:
            if event['payload']['action']:
                action = event['payload']['action']
        except:
            pass

        try:
            if event['payload']['ref_type']:
                action = event['payload']['ref_type']
        except:
            pass
        
        event_repo_key = type + ',' + repo + ',' + action
        activities.setdefault(event_repo_key, 0)
        activities[event_repo_key] = activities[event_repo_key] + 1

    return activities
