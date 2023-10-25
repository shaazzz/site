# Shaazzz Website

Powered by [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)

## Requirements

You need python requirements only if you want to locally serve the blog.

```console
$ pip install -r requirements.txt
```

## Build

Build the whole blog (including blog posts, pages, and archive page):

```console
$ make
```

Preview the blog locally:

```console
$ make serve
```

Remove all build files:

```console
$ make clean
```

## Publish a blog post

Write your blog in a markdown file (`.md`), inside `raw/`. Filename should follow this convention: `YEAR-MONTH-DAY-TITLE.md`. The file content looks like this.

```markdown
---
blog:
    author: # author name
    date: [YEAR, MONTH, DAY, HOUR, MINUTE] # date of last modification
---

# Blog title here

Blog contents...
```

## Add archive entry

Just edit `archive.yml`. The entry will be automatically added on build.
