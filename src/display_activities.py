from utils.word_pluralizer import pluralize


def display(activities: dict):
    '''Display the activities from a dictionary {'event,repo': count}'''
    print('Output:')
    for event_repo_key, count in activities.items():
        keys = event_repo_key.split(',')
        event, repo = keys[0], keys[1]
        match event:
            case 'CommitCommentEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'CreateEvent':
                print(f'- Created {count} {pluralize("event", count)} in {repo}')
            case 'DeleteEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'ForkEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'GollumEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'IssueCommentEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'IssuesEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'MemberEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PublicEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PullRequestEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PullRequestReviewEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PullRequestReviewCommentEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PullRequestReviewThreadEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'PushEvent':
                print(f'- Pushed {count} {pluralize("commit", count)} into {repo}')
            case 'ReleaseEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'SponsorshipEvent':
                print(f'- (!) {event} {count} {repo}')
            case 'WatchEvent':
                print(f'- (!) {event} {count} {repo}')
            case _:
                print(f'- Unsupported Event')
