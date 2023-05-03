RAWPOSTS=${wildcard raw/*.md}
POSTS=${patsubst raw/%.md,docs/blog/post/%.md,${RAWPOSTS}}
FIRSTPAGE=docs/index.md
ARCHIVEPAGE=docs/archive.md
ARCHIVEFILE=archive.yml

all: ${POSTS} ${FIRSTPAGE} ${ARCHIVEPAGE}
	@echo done!

serve: all
	mkdocs serve

clean:
	rm -rf docs/blog/ docs/archive.md

.PHONY: all serve clean

docs/blog/post/%.md: raw/%.md scripts/style.py
	@mkdir -p $(@D)
	python -m scripts style -l $< -d $@

${FIRSTPAGE}: ${POSTS} scripts/pagemaker.py
	@mkdir -p $(@D)
	python -m scripts page-maker

${ARCHIVEPAGE}: ${ARCHIVEFILE} scripts/archive.sh scripts/generate_table.py
	@mkdir -p $(@D)
	bash ./scripts/archive.sh $< > $@
