import re
import sys


USERNAME_PATTERN = '^[a-zA-Z0-9-]*$'


def validate(username: str):
    '''GitHub usernames can only have alphanumeric characters and dashes'''
    if not bool(re.search(USERNAME_PATTERN, username)):
        print ('error: Invalid GitHub username')
        sys.exit()
