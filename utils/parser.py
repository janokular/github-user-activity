import argparse


def parse_arguments():
    '''Parse arguments needed for the program's logic'''
    parser = argparse.ArgumentParser(description='Program used to fetch the recent activity of a GitHub user')

    parser.add_argument('USERNAME')

    return parser.parse_args()
