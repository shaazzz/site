import frontmatter

from persiantools import digits
from pathlib import Path


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

def main():
    for post in Path('scripts/raw/').glob('*.md'):
        author, date, content = read_file(post)
        with open(f'docs/blog/post/{post.name}', 'w') as file:
            file.write(style(content, author, date))

if __name__ == "__main__":
    main()