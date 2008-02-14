TARGET_PREFIX=../public_html/ibofobi.dk

SOURCES=$(shell find pages -type f | sed s,^pages,,) \
        $(addsuffix /index,$(addprefix /blog/archive/,$(shell blog/published)))
PAGES=$(addsuffix .html, $(basename ${SOURCES}))
TARGETS=$(addprefix ${TARGET_PREFIX},${PAGES}) \
	${TARGET_PREFIX}/blog/index.html

.PHONY: all

all: ${TARGETS}

${TARGET_PREFIX}/%.html.work: pages/%.html html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@./metal < $< | ./to-html > $@

${TARGET_PREFIX}/blog/archive/%/index.html.work: blog/% html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@./metal --context 'post=blog:read_post("$(subst blog/,,$<)")' < blog/post.xhtml | ./to-html > $@

${TARGET_PREFIX}/blog/index.html.work: blog/index
	@echo blog/recent
	@./metal --context 'posts=blog:recent' < blog/recent.xhtml | ./to-html > $@

%: %.work
	@mv -f $< $@
