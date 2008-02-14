PYTHONPATH=blog

TARGET_PREFIX=../public_html/ibofobi.dk

SOURCES=$(shell find pages -type f | sed s,^pages,,) \
        $(addsuffix /index,$(addprefix /blog/archive/,$(shell blog/published)))
PAGES=$(addsuffix .html, $(basename ${SOURCES}))
TARGETS=$(addprefix ${TARGET_PREFIX},${PAGES})

.PHONY: all

all: ${TARGETS}

${TARGET_PREFIX}/%.html.work: pages/%.html html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@./metal --macros page.html < $< | ./to-html > $@

${TARGET_PREFIX}/blog/archive/%/index.html.work: blog/% html.xsl page.html metal
	@echo $<
	@mkdir -p $(dir $@)
	@blog/to-metal $(subst blog/,,$<) | ./metal --macros page.html | ./to-html > $@

%: %.work
	@mv -f $< $@
