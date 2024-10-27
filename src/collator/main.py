import argparse
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=str)
    parser.add_argument("params", type=str)
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    # load arguments
    with open(args.params, "r") as f:
        parameters = yaml.load(f, Loader=yaml.SafeLoader)
    print(parameters)
