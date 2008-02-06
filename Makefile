SOURCE_PREFIX=pages
TARGET_PREFIX=../public_html/ibofobi.dk

SOURCES=$(shell find pages -type f | sed s,^${SOURCE_PREFIX},,)
PAGES=$(addsuffix .html, $(basename ${SOURCES}))
TARGETS=$(addprefix ${TARGET_PREFIX},${PAGES})

all: ${TARGETS}

${TARGET_PREFIX}/%.html: ${SOURCE_PREFIX}/%.html html-doctype html.xsl page.html metal
	@echo $@
	@mkdir -p $(dir $@)
	@cat html-doctype > $@.work
	@./metal --macros page.html < $^ | xsltproc --nonet --novalid html.xsl - >> $@.work
	@mv -f $@.work $@
