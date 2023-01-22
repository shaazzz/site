# Shaazzz Website

Powered by [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)

## Requirements

Install python dependencies:

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

Write your blog in a markdown file (`.md`), outside of project directory. Your file should look like this.

```markdown
---
blog:
    author: # author name
---

# Blog title here

Blog contents...
```

Then run this command to add your file to the blogs section.

```console
$ python -m scripts publish -f /path/to/post.md
```

At last, add, commit, and push the changes.

## Add archive entry

Just edit `archive.yml`. The entry will be automatically added on build.
