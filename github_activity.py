#!/bin/env python3


from utils.parser import parse_arguments
from utils.validate_username import validate
from src.fetch_response import fetch
from src.format_response import format
from src.display_activities import display


def main():
    args = parse_arguments()

    USERNAME = args.USERNAME

    validate(USERNAME)

    display(format(fetch(USERNAME)))

if __name__ == '__main__':
    main()
