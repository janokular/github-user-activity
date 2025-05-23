def display(activities):
    '''Display user's activities'''
    print('Output:')

    for event_repo_key, count in activities.items():
        # Split the keys separeted with ','
        # keys = ['event', 'repo']
        keys = event_repo_key.split(',')
        match keys[0]:
            case 'CommitCommentEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'CreateEvent':
                if count == 1:
                    print(f'- Created {count} event in {keys[1]}')
                else:
                    print(f'- Created {count} events in {keys[1]}')
            case 'DeleteEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'ForkEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'GollumEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'IssueCommentEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'IssuesEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'MemberEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PublicEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewCommentEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PullRequestReviewThreadEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'PushEvent':
                if count == 1:
                    print(f'- Pushed {count} commit into {keys[1]}')
                else:
                    print(f'- Pushed {count} commits into {keys[1]}')
            case 'ReleaseEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'SponsorshipEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case 'WatchEvent':
                if count == 1:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
                else:
                    print(f'- (!) {keys[0]} {count} {keys[1]}')
            case _:
                print(f'- Unsupported Event')
