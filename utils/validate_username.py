import re
import sys


def validate(username: str):
    '''GitHub usernames can alphanumeric characters and dashes'''
    if not bool(re.search('^[a-zA-Z0-9-]*$', username)):
        print('Invalid GitHub username')
        sys.exit()
