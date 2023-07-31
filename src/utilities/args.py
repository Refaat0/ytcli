from argparse import ArgumentParser, Namespace

"""
    This function defines this applications arguments and,
    returns a Namespace of the argument called in the console
"""
def args() -> Namespace:
    # initialize the ArgumentParser
    parser = ArgumentParser(
        prog="ytcli",
        description="an original description",
        epilog="an original epilog"
    )

    # by adding arguments to the application_parser instead of the parser we can insure that,
    # only one argument can be called at a time
    application_parser = parser.add_mutually_exclusive_group()

    application_parser.add_argument(
        "--1080p",
        help="Downloads a Youtube video at the 1080p resolution",
        metavar="str: A Youtube Video Link"
    )

    application_parser.add_argument(
        "--720p",
        help="Downloads a Youtube video at the 720p resolution",
        metavar="str: A Youtube Video Link"
    )

    application_parser.add_argument(
        "--160kbps",
        help="Downloads a Youtube video at 160kbps",
        metavar="str: A Youtube Video Link"
    )

    application_parser.add_argument(
        "--128kbps",
        help="Downloads a Youtube video at 128kbps",
        metavar="str: A Youtube Video Link"
    )

    application_parser.add_argument(
        "--70kbps",
        help="Downloads a Youtube video at 70kbps",
        metavar="str: A Youtube Video Link"
    )

    application_parser.add_argument(
        "--50kbps",
        help="Downloads a Youtube video at 50kbps",
        metavar="str: A Youtube Video Link"
    )

    return parser.parse_args()
