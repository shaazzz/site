import argparse
from argparse import ArgumentParser

from . import export, generate_table, style, pagemaker

def main():
    main_parser = ArgumentParser(description='shaazzz util scripts')

    modules = {
        'export': export,
        'generate-table': generate_table,
        'style': style,
        'page-maker': pagemaker,
    }
    subparsers = main_parser.add_subparsers(required=True)
    for cmd, mod in modules.items():
        parser = subparsers.add_parser(cmd)
        mod.init(parser)

    args = main_parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
