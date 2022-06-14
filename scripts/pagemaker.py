import sys
from argparse import ArgumentParser
from pathlib import Path

import frontmatter
from persiantools import digits

root = Path('docs/blog')

def get_files():
    return list(root.glob('post/*.md'))

def read_meta(file):
    post = frontmatter.load(file)
    return post.metadata["blog"]

def get_metafiles(files):
    result = []
    for file in files:
        result.append((file, read_meta(file)))
    return result

def make_all(metafiles):
    n = len(metafiles)
    k = 8
    batches = []
    for i in range(0, n, k):
        batches.append(metafiles[i:i+k])
    for i, batch in enumerate(batches):
        make_page(i+1, batch, len(batches))
    make_page(1, batches[0], len(batches),
        title="# بلاگ",
        result_path="docs/index.md"
    )

def make_page(index, metafiles, n_page, title=None, result_path=None):
    title = title or digits.en_to_fa(f"# صفحه {index}")
    content = title + '\n'
    for post in metafiles:
        content += read_content(post[0])
    content += make_pagination(index, n_page)
    result_path = result_path or f"docs/blog/page/{index}.md"
    with open(result_path, 'w') as file:
        file.write(content)

def read_content(file):
    post = frontmatter.load(file)
    content = post.content.split('\n')
    _, loc = str(file).split('/', 1)
    loc = f'/{loc[:-3]}'
    for i in range(len(content)):
        if content[i][0:2] == '# ':
            _, title = content[i].split(' ', 1)
            content[i] = f"## [{title}]({loc})"
    content.append('---\n')
    content = '\n'.join(content)
    return content

def make_pagination(index, n_page):
    result = '<div class="blog-page" markdown>\n\n'
    sant = lambda x : digits.en_to_fa(str(x))
    path = lambda x : f'/blog/page/{x}'
    if index > 2:
        result += f'[:material-arrow-collapse-left: {sant(1)}]({path(1)})\n'
    if index > 1:
        result += f'[:material-arrow-left: {sant(index-1)}]({path(index-1)})\n'
    result += sant(index) + '\n'
    if index < n_page:
        result += f'[{sant(index+1)} :material-arrow-right:]({path(index+1)})\n'
    if index < n_page-1:
        result += f'[{sant(n_page)} :material-arrow-collapse-right:]({path(n_page)})\n'
    result += '\n</div>'
    return result

def main(args):
    (root/'page').mkdir(exist_ok=True)
    files = get_files()
    metafiles = get_metafiles(files)
    metafiles.sort(key=lambda u: u[1]['date'], reverse=True)
    make_all(metafiles)

def init(parser: ArgumentParser):
    parser.set_defaults(func=main)