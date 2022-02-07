import requests as req
from bs4 import BeautifulSoup
import urllib
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
    global soup
    post = fetch_post(href)
    soup = BeautifulSoup(post.text, 'lxml')

    content = parse_content(soup)
    content = str(content)
    content = content.replace('<p> </p>', '')

    title = soup.select_one('.post .title a').text
    author = soup.select_one('.author').text
    date = parse_date("/1400/04/22/quera_contest1", soup)

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

def markdown_post(href):
    title, author, date, content = parse_post(href)
    return f"""---
blog:
    author: {author}
    date: {date}
---
# {title}

{content}

{encode_info(author, date)}
"""

def write_post(href):
    filename = sanitize(href)
    with open(f"output/{filename}.md", 'w') as file:
        file.write(markdown_post(href))

links = []
for i in range(1, 30):
    links += list(find_links(fetch_page(i)))

for l in links:
    write_post(l)