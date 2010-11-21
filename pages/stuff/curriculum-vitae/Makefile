.PHONY: all

all: cv.pdf

cv.pdf: cv.dvi
	dvipdf cv.dvi cv.pdf

cv.dvi: cv.tex
	latex cv.tex < /dev/null
