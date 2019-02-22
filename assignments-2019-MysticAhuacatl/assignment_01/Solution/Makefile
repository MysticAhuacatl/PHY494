NAME := solution_01

RST := $(NAME).rst
PDF := $(NAME).pdf

%.pdf: %.txt
	rst2pdf $<

%.pdf: %.rst
	pandoc $< -o $@

.phony: all see

all: $(PDF)

see: $(PDF)
	open $^


