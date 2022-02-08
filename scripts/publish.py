from argparse import ArgumentParser
from pathlib import Path
from frontmatter import Frontmatter
from persiantools import digits, jdatetime

def encode_info(author, date):
    date = list(map(str, date))
    for i in range(1, 5):
        if len(date[i]) < 2:
            date[i] = "0" + date[i]
    date = map(digits.en_to_fa, date)
    date = list(date)

    return f"""<div class="blog-info">
    <div class="blog-author">{author}</div>
    <div class="blog-date">{date[0]}/{date[1]}/{date[2]} {date[3]}:{date[4]}</div>
</div>
"""

def read_file(file):
    post = Frontmatter.read_file(file)
    author = None
    date = None
    if "blog" in post["attributes"]:
        attrs = post["attributes"]["blog"]
        if "author" in attrs:
            author = attrs["author"]
        if "date" in attrs:
            date = attrs["date"]
    return author, date, post["body"]

def get_now():
    now = jdatetime.JalaliDateTime.now()
    return [now.year, now.month, now.day, now.hour, now.minute]

def markdown_post(content, author, date):
    return f"""---
blog:
    author: {author}
    date: {date}
---
{content}

{encode_info(author, date)}
"""

def write_file(filename, content):
    path = f'docs/blog/post/{filename}'
    print(f"Writing to {path}")
    with open(path, 'w') as file:
        file.write(content)

def get_title(content):
    content = content.split('\n')
    for i in range(len(content)):
        if content[i][0:2] == '# ':
            _, title = content[i].split(' ', 1)
            return title

def get_filename(content, date):
    title = get_title(content)
    title.replace(' ', '-')
    date = list(map(str, date))
    for i in range(1, 3):
        if len(date[i]) < 2:
            date[i] = '0'+date[i]
    return f'{date[0]}-{date[1]}-{date[2]}-{title}.md'

def main():
    global args
    argparse = ArgumentParser(description='publish blog post')
    argparse.add_argument(
        '-f','--file',
        type=Path,
        help='Content of blog post in markdown format (required)',
        required=True
    )
    argparse.add_argument(
        '-a','--author',
        type=str,
        help='Author of blog post',
    )
    argparse.add_argument(
        '-d','--date',
        type=str,
        help='Blog published datetime, in this format: "{year} {month} {day} {hour} {minute} (optional, default is the current time)'
    )
    args = argparse.parse_args()
    author, date, content = read_file(args.file)
    author = author or args.author
    date = date or args.date or get_now()

    if not author:
        raise Exception("No author")
    if not date:
        raise Exception("No date")

    filename = get_filename(content, date)
    write_file(filename, markdown_post(content, author, date))

if __name__ == "__main__":
    main()