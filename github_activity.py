#!/bin/env python3


from utils.parser import parse_arguments
from utils.username_validator import validate
from src.fetch_response import fetch
from src.format_response import format
from src.display_activities import display


def main():
    args = parse_arguments()

    USERNAME = args.USERNAME

    validate(USERNAME)

    response = fetch(USERNAME)

    activities = format(response)

    display(activities)

if __name__ == '__main__':
    main()
