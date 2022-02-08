# Shaazzz Website

Powered by [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)

## How to publish a blog post

First you should install dependencies. You have to run this command.

```console
$ pip install -r scripts/requirements.txt
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
$ python scripts/publish.py -f /path/to/post.md
```

At last, add, commit, and push the changes.