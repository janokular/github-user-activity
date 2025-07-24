import re
import sys


def validate(username: str):
    '''GitHub usernames can only have alphanumeric characters and dashes'''
    if not bool(re.search('^[a-zA-Z0-9-]*$', username)):
        print ('error: Invalid GitHub username')
        sys.exit()
