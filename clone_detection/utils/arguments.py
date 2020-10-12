import argparse


def get_args():
    """Get the arguments for the program."""
    parser = argparse.ArgumentParser(
        description='Clone Detection')

    parser.add_argument('--f', nargs='+', type=str,
                        help='Files for detecting clones')

    return parser.parse_args()
