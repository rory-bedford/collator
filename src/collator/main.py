import argparse
import yaml
import importlib.util
import os
import sys


def collate(inputs, outputs):
    def decorator(func):
        func.collated = True
        return func

    return decorator


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

    # import script
    script_path = args.script
    module_name = os.path.splitext(os.path.basename(script_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
