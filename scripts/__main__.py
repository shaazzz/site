import argparse
from argparse import ArgumentParser

from . import export

def main():
    main_parser = ArgumentParser(description='shaazzz util scripts')

    modules = {
        'export': export
    }
    subparsers = main_parser.add_subparsers()
    for cmd, mod in modules.items():
        parser = subparsers.add_parser(cmd)
        mod.init(parser)

    args = main_parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()