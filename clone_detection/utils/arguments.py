import argparse


def get_args():
    """Get the arguments for the program."""
    parser = argparse.ArgumentParser(
        description='Clone Detection')

    parser.add_argument('--f', nargs='+', type=str, default=[],
                        help='Files for detecting clones')
    parser.add_argument('--d', nargs='+', type=str, default='',
                        help='Directory of projects for detecting clones')

    return parser.parse_args()
