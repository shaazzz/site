from argparse import ArgumentParser
from pathlib import Path

import frontmatter
from persiantools import digits


def encode_info(author, date):
    date = list(map(str, date))
    for i in range(1, 5):
        if len(date[i]) < 2:
            date[i] = "0" + date[i]
    date = map(digits.en_to_fa, date)
    date = list(date)

    return f"""<div class="blog-info" markdown>
<span class="blog-author">
:fontawesome-regular-user: {author}
</span>
<span class="blog-date">
:octicons-calendar-24: {date[0]}/{date[1]}/{date[2]} · :octicons-clock-24: {date[3]}:{date[4]}
</span>
</div>
"""

def style(content, author, date):
    return f"""---
blog:
    author: {author}
    date: {date}
template: blog.html
---
{content}
{encode_info(author, date)}
"""

def raw_style(content, author, date):
    return f"""---
blog:
    author: {author}
    date: {date}
---
{content}
"""

def read_file(file):
    post = frontmatter.load(file)
    metadata = post.metadata
    author = None
    date = None
    if "blog" in metadata:
        attrs = metadata["blog"]
        if "author" in attrs:
            author = attrs["author"]
        if "date" in attrs:
            date = attrs["date"]
    return author, date, post.content

def main(args):
    post = args.location
    author, date, content = read_file(post)
    with open(args.destination, 'w') as file:
        file.write(style(content, author, date))

def init(parser: ArgumentParser):
    parser.add_argument(
        '-l', '--location',
        help='location of raw blog post',
        required=True,
        type=Path
    )
    parser.add_argument(
        '-d', '--destination',
        help='destination of blog post',
        required=True,
        type=Path
    )
    parser.set_defaults(func=main)
