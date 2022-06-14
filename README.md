# Shaazzz Website

Powered by [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)

## Publish a blog post

First you should install dependencies. You have to run this command.

```console
$ pip install -r requirements.txt
```

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

Edit `archive.yml`. This command will output the markdown table for archive section.
```console
$ python -m scripts generate-table -f archive.yml
```

Copy the output and paste it in `docs/archive/index.md`.

## Preview blog

```console
$ pip install -r requirements.txt
$ pip install mkdocs-material
$ python -m scripts page-maker
$ mkdocs serve
```
