from collections import Counter


def format(response: list[dict]) -> list[dict]:
    '''
    Format the response
    by counting user events inside each repository
    '''
    events = get_events_from_response(response)
    counted_events = count_event_occurrences(events)
    return counted_events


def get_events_from_response(response: list[dict]) -> list[dict]:
    '''
    Get event type, repository name
    and action from the response
    return it as a list[dict]
    '''
    events = []
    
    for e in response:
        event_type = e['type']
        repo = e['repo']['name']
        action = ''

        try:
            if e['payload']['action']:
                action = e['payload']['action']
        except:
            pass

        try:
            if e['payload']['ref_type']:
                action = e['payload']['ref_type']
        except:
            pass
        
        events.append({
            'event_type': event_type,
            'repo': repo,
            'action': action,
        })

    return events


def count_event_occurrences(events: list[dict]) -> list[dict]:
    '''
    Count event occurrences, remove duplicates 
    and add occurrence count to the list[dict]
    '''
    counter = Counter(
        (
            e['event_type'], e['repo'], e['action']
        ) for e in events
    )

    return [
        {
            'event_type': event_type,
            'repo': repo,
            'action': action,
            'count': count,
        }
        for (
            event_type, repo, action
        ), count in counter.items()
    ]
