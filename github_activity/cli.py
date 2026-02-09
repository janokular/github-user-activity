from argparse import ArgumentParser


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog='github_activity',
        description='GitHub User Activity - fetch the recent activity of a GitHub user',
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if False:
        args.func(args)
    else:
        parser.print_help()
