from utils.word_pluralizer import pluralize


def display(activities: dict):
    '''Display the activities from a dictionary {'event_type,repo,detail': count}'''
    print('Output:')
    for key, count in activities.items():
        keys = key.split(',')
        event_type, repo, detail = keys[0], keys[1], keys[2]
        match event_type:
            case 'CommitCommentEvent':
                print(f'- {detail.capitalize()} {count} commit {pluralize("comment", count)} inside {repo}')
            case 'CreateEvent':
                print(f'- Created {count} {pluralize(detail, count)}{" in" if detail != "repository" else ""} {repo}')
            case 'DeleteEvent':
                print(f'- Deleted {count} {pluralize(detail, count)} inside {repo}')
            case 'ForkEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'GollumEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'IssueCommentEvent':
                print(f'- {detail.capitalize()} {count} issue {pluralize("comment", count)} in {repo}')
            case 'IssuesEvent':
                print(f'- {detail.capitalize()} {count} {pluralize("issue", count)} inside {repo}')
            case 'MemberEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'PublicEvent':
                print(f'- {count} private repository {"was" if count == 1 else "were"} made public')
            case 'PullRequestEvent':
                print(f'- {detail.capitalize()} {count} pull {pluralize("request", count)} inside {repo}')
            case 'PullRequestReviewEvent':
                print(f'- {detail.capitalize()} {count} pull request {pluralize("review", count)} in {repo}')
            case 'PullRequestReviewCommentEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'PullRequestReviewThreadEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'PushEvent':
                print(f'- Pushed {count} {pluralize("commit", count)} into {repo}')
            case 'ReleaseEvent':
                print(f'- {detail.capitalize()} {count} {repo}')
            case 'SponsorshipEvent':
                print(f'- (!) {count} {repo} {detail}')
            case 'WatchEvent':
                print(f'- (!) {count} {repo} {detail}')
            case _:
                print(f'- Unsupported Event')
