from argparse import ArgumentParser

from .handlers.request_handler import request_handler


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog='github_activity',
        description='GitHub User Activity - fetch the recent activity of a GitHub user',
    )

    parser.add_argument(
        'username',
        type=str,
        help='username to look up',
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.username:
        request_handler(args.username)
    else:
        parser.print_help()
