import http.client


def fetch(username: str):
    '''Fetch data from GitHub REST API'''
    host = 'api.github.com'
    conn = http.client.HTTPSConnection(host)
    conn.request('GET', '/users/{}/events/'.format(username), headers={'Host': host, 'User-Agent': 'request'})
    return conn.getresponse()


def display(username):
    '''Display the user's recent activity'''
    response = fetch(username)
    print(response.read())
