RAWPOSTS=${wildcard raw/*.md}
POSTS=${patsubst raw/%.md,docs/blog/post/%.md,${RAWPOSTS}}
FIRSTPAGE=docs/index.md
ARCHIVEPAGE=docs/archive/index.md
ARCHIVEFILE=archive.yml

all: ${POSTS} ${FIRSTPAGE} ${ARCHIVEPAGE}
	@echo done!
.PHONY: all

serve: all
	mkdocs serve
.PHONY: serve

docs/blog/post/%.md: raw/%.md scripts/style.py
	mkdir -p ${dir $@}
	python -m scripts style -l $< -d $@

${FIRSTPAGE}: ${POSTS} scripts/pagemaker.py
	mkdir -p ${dir $@}
	python -m scripts page-maker

${ARCHIVEPAGE}: ${ARCHIVEFILE} scripts/archive.sh scripts/generate_table.py
	mkdir -p ${dir $@}
	bash ./scripts/archive.sh $< > $@

clean:
	rm -rf docs/blog/ docs/archive/
.PHONY: clean
