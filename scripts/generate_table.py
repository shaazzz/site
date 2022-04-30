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

with open('scripts/archive.yml', 'r') as file:
    data = yaml.safe_load(file)

table = generate_head(data['head'])
for row in data["body"]:
    table += generate_row(row)
print(table)
