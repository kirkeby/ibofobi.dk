TARGET_PREFIX=../public_html/ibofobi.dk

SOURCES=$(shell find pages -type f | egrep -v '~|/\.' | sed s,^pages,,) \
        $(addsuffix /index,$(addprefix /blog/archive/,$(shell blog/published)))
PAGES=$(addsuffix .html, $(basename ${SOURCES}))
TARGETS=$(addprefix ${TARGET_PREFIX},${PAGES}) \
	${TARGET_PREFIX}/blog/index.html \
	${TARGET_PREFIX}/blog/feeds/latest/index.xml

.PHONY: all

all: ${TARGETS}

${TARGET_PREFIX}/%.html.work: pages/%.html html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@./metal --xhtml-doctype < $< | ./to-html > $@

${TARGET_PREFIX}/%.html.work: pages/%.txt html.xsl page.html metal markdown
	@echo $<
	@mkdir -p $(dir $@)
	@./markdown < $< | ./metal --xhtml-doctype | ./to-html > $@

${TARGET_PREFIX}/blog/archive/%/index.html.work: blog/% html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@./metal --xhtml-doctype --context 'post=blog:read_post("$(subst blog/,,$<)")' < blog/post.xhtml | ./to-html > $@

${TARGET_PREFIX}/blog/index.html.work: blog/index
	@echo blog/
	@./metal --xhtml-doctype --context 'posts=blog:recent' < blog/recent.xhtml | ./to-html > $@

${TARGET_PREFIX}/blog/feeds/latest/index.xml: blog/index blog/atom.xml
	@echo blog/feeds/latest/
	@mkdir -p $(dir $@)
	@./metal --context 'posts=blog:recent' --context 'blog=blog:info' \
		< blog/atom.xml > $@

%: %.work
	@mv -f $< $@
