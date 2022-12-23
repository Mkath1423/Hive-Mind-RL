import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="the config file for running the program",
                    type=str)
args = parser.parse_args()


def get_arg(arg):
    if hasattr(args, arg):
        return getattr(args, arg)
    return None


