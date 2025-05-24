import argparse


def parse_arguments():
    '''Parse user's arguments'''
    parser = argparse.ArgumentParser(description='Program used to fetch the recent activity of a GitHub user')

    parser.add_argument('USERNAME')

    return parser.parse_args()
