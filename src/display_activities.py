def display(activities):
    '''Display user's activities'''
    print('Output:')

    for event_repo_key, count in activities.items():
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
