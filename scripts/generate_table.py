from argparse import ArgumentParser
from pathlib import Path

import yaml

def generate_head(head):
    return f"|{'|'.join(head)}|\n|{':-:|'*len(head)}\n"

def get_only_key(json):
    for key in json:
        return key
    raise KeyError("empty json")

def generate_cell(cell):
    if type(cell) == str:
        return cell
    if cell is None:
        return ''
    links = []
    for text, link in cell.items():
        links.append(f'[{text}]({link})')
    return '، '.join(links)

def generate_row(row):
    return f"|{'|'.join(map(generate_cell, row))}|\n"

def main(args):
    with open(args.file, 'r') as file:
        data = yaml.safe_load(file)

    table = generate_head(data['head'])
    for row in data["body"]:
        table += generate_row(row)
    print(table)

def init(parser: ArgumentParser):
    parser.add_argument(
        '-f', '--file',
        help='location of archive.yml',
        required=True,
        type=Path
    )
    parser.set_defaults(func=main)