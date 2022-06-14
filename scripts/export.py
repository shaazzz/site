import urllib
from argparse import ArgumentParser
from pathlib import Path

import requests as req
from bs4 import BeautifulSoup
from persiantools import digits


def fetch_page(n):
    print(f"fetch {n}")
    return req.get(f"http://blog.shaazzz.ir/?page={n}")

def fetch_post(href):
    print(f"fetch {href}")
    return req.get(f"http://blog.shaazzz.ir{href}")

def find_links(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    for post in soup.find_all(class_="post"):
        a = post.find(href=True)
        href = a["href"]
        yield href

def sanitize(href):
    href = href[1:]
    href = href.replace('/', '-')
    href = urllib.parse.unquote(href)
    return href

def parse_post(href):
    post = fetch_post(href)
    soup = BeautifulSoup(post.text, 'lxml')

    content = parse_content(soup)
    content = str(content)
    content = content.replace('<p> </p>', '')

    title = soup.select_one('.post .title a').text
    author = soup.select_one('.author').text
    date = parse_date(href, soup)

    title, author = map(digits.en_to_fa, [title, author])

    return title, author, date, content

def parse_date(href, soup):
    _, y, m, d, *_ = href.split('/')
    y, m, d = map(int, [y, m, d])

    tm = soup.select_one('.date_title').text.split()
    hr, mn = digits.fa_to_en(tm[-2]).split(':')
    hr, mn = map(int, [hr, mn])

    if tm[-1] == 'ب.ظ':
        hr += 12
    return [y, m, d, hr, mn]

def parse_content(soup):
    content = soup.select_one('.post .cnt')
    for tag in content.find_all():
        del tag["style"]
    for tag in ['font', 'span']:
        for match in content.find_all(tag):
            match.replaceWithChildren()
    return content

def markdown_post(href):
    title, author, date, content = parse_post(href)
    return f"""---
blog:
    author: {author}
    date: {date}
---
# {title}

{content}
"""

def write_post(loc: Path, href):
    filename = sanitize(href)
    with open(loc / f"{filename}.md", 'w') as file:
        file.write(markdown_post(href))

def main(args):
    links = []
    for i in range(1, args.num_pages+1):
        links += list(find_links(fetch_page(i)))

    for l in links:
        write_post(args.location, l)

def init(parser: ArgumentParser):
    parser.add_argument(
        '-l', '--location',
        help='location to save raw blog posts',
        required=True,
        type=Path
    )
    parser.add_argument(
        '-n', '--num-pages',
        help='number of blog pages',
        required=True,
        type=int
    )
    parser.set_defaults(func=main)
