STORAGE_PATH?=~/Zotero/storage

all: prepare run

prepare:
	rm -f pdfs.txt
	rm -f refs/*
	rm -f graph/*
	mkdir -p refs
	mkdir -p graph

run:
	bash extract_refs.sh $(STORAGE_PATH)
	python3 build_graph.py
	cat refs.txt | sort | uniq -c | sort -h
