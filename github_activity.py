#!/bin/env python3


import argparse
from src.activity import display


def main():
    parser = argparse.ArgumentParser(description='Program used to fetch the recent activity of a GitHub user')

    parser.add_argument('USERNAME')

    args = parser.parse_args()

    display(args.USERNAME)

if __name__ == '__main__':
    main()
