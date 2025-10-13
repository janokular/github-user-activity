from utils.word_pluralizer import pluralize


def display(activities: dict):
    '''Display the activities from a dictionary {'event_type,repo,action': count}'''
    print('Output:')
    for key, count in activities.items():
        keys = key.split(',')
        event_type, repo, action = keys[0], keys[1], keys[2]
        match event_type:
            case 'CommitCommentEvent':
                print(f'- {action.capitalize()} {count} commit {pluralize("comment", count)} inside {repo}')
            case 'CreateEvent':
                print(f'- Created {count} {pluralize(action, count)}{" in" if action != "repository" else ""} {repo}')
            case 'DeleteEvent':
                print(f'- Deleted {count} {pluralize(action, count)} inside {repo}')
            case 'ForkEvent':
                print(f'- Forked repository {repo}')
            case 'GollumEvent':
                print(f'- {action.capitalize()} wiki page in {repo}')
            case 'IssueCommentEvent':
                print(f'- {action.capitalize()} {count} issue {pluralize("comment", count)} in {repo}')
            case 'IssuesEvent':
                print(f'- {action.capitalize()} {count} {pluralize("issue", count)} inside {repo}')
            case 'MemberEvent':
                print(f'- {action.capitalize()} {count} {pluralize("member", count)} to {repo}')
            case 'PublicEvent':
                print(f'- {count} private repository {"was" if count == 1 else "were"} made public')
            case 'PullRequestEvent':
                print(f'- {action.capitalize()} {count} pull {pluralize("request", count)} inside {repo}')
            case 'PullRequestReviewEvent':
                print(f'- {action.capitalize()} {count} pull request {pluralize("review", count)} in {repo}')
            case 'PullRequestReviewCommentEvent':
                print(f'- {action.capitalize()} {count} pull request review {pluralize("comment", count)} in {repo}')
            case 'PullRequestReviewThreadEvent':
                print(f'- {action.capitalize()} {count} comment {pluralize("thread", count)} in {repo}')
            case 'PushEvent':
                print(f'- Pushed {count} {pluralize("commit", count)} into {repo}')
            case 'ReleaseEvent':
                print(f'- {action.capitalize()} {count} {repo}')
            case 'SponsorshipEvent':
                print(f'- {action.capitalize()} {count} sponsorship {pluralize("event", count)} in {repo}')
            case 'WatchEvent':
                print(f'- {action.capitalize()} subscribing to repository {repo}')
            case _:
                print(f'- Unsupported Event')
