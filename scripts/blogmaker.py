from pathlib import Path
from frontmatter import Frontmatter
from persiantools import digits

root = Path('docs/blog')

def get_files():
    return list(root.glob('post/*.md'))

def read_meta(file):
    post = Frontmatter.read_file(file)
    return post["attributes"]["blog"]

def get_metafiles(files):
    result = []
    for file in files:
        result.append((file, read_meta(file)))
    return result

def make_all(metafiles):
    n = len(metafiles)
    k = 8
    timer = 0
    for i in range(0, n, k):
        timer += 1
        make_page(
            index=timer,
            metafiles=metafiles[i:i+k],
            prv=(i>0),
            nxt=(i+k<n)
        )
        if timer == 1:
            make_page(
                index=timer,
                metafiles=metafiles[i:i+k],
                prv=(i>0),
                nxt=(i+k<n),
                title="# بلاگ",
                result_path="docs/index.md"
            )

def make_page(index, metafiles, prv, nxt, title=None, result_path=None):
    title = title or digits.en_to_fa(f"# صفحه {index}")
    content = title + '\n'
    for post in metafiles:
        content += read_content(post[0])
    content += make_pagination(index, prv, nxt)
    result_path = result_path or f"docs/blog/page/{index}.md"
    with open(result_path, 'w') as file:
        file.write(content)

def read_content(file):
    post = Frontmatter.read_file(file)
    content = post["body"].split('\n')
    _, loc = str(file).split('/', 1)
    loc = '/' + loc[:-3]
    for i in range(len(content)):
        if content[i][0:2] == '# ':
            _, title = content[i].split(' ', 1)
            content[i] = f"## [{title}]({loc})"
    content.append('---\n')
    content = '\n'.join(content)
    return content

def make_pagination(index, prv, nxt):
    result = '<div class="blog-page" markdown>\n\n'
    if prv:
        s = digits.en_to_fa(str(index-1))
        result += f'[:octicons-arrow-left-24: {s}](/blog/page/{index-1})\n'
    result += digits.en_to_fa(str(index)) + '\n'
    if nxt:
        s = digits.en_to_fa(str(index+1))
        result += f'[{s} :octicons-arrow-right-24:](/blog/page/{index+1})\n'
    result += '\n</div>'
    return result

files = get_files()
metafiles = get_metafiles(files)
metafiles.sort(key=lambda u: u[1]['date'], reverse=True)
make_all(metafiles)