all: build
build:
	pdflatex thesis.tex
	pdflatex thesis.tex
lib: lib/newllang.pdf
lib/newllang.pdf:
	mkdir -p lib
	cd lib
	fetch -o lib/newllang.pdf https://www.mccme.ru/free-books/llang/newllang.pdf
clean:
	rm *.pdf *.toc *.aux *.log *.out *.tex~ *synctex*
