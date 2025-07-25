def format(response: list):
    '''
    Format the response by counting events inside each repository\n
    and return it as a dictionary {'event_type,repo,detail': count}
    '''
    activities = {}
    
    for event in response:
        type = event['type']
        repo = event['repo']['name']
        detail = ''

        try:
            if event['payload']['action']:
                detail = event['payload']['action']
        except:
            pass

        try:
            if event['payload']['ref_type']:
                detail = event['payload']['ref_type']
        except:
            pass
        
        event_repo_key = type + ',' + repo + ',' + detail
        activities.setdefault(event_repo_key, 0)
        activities[event_repo_key] = activities[event_repo_key] + 1

    return activities
