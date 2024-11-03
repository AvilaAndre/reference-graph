#!/bin/zsh

declare -a PDFS=()

PDFS="pdfs.txt"

# Path to Zotero storage
CMD="ls ${1}/**/*.pdf"

eval "$CMD" > $PDFS

IFS=$'\n'
for file in `cat $PDFS`; do
	FILENAME=`basename $file .pdf`
	echo $FILENAME

	anystyle find $file | jq -r ".[] | {title: .title[0], date: .date[0], author:.author, type:.type}| @json" > "refs/${FILENAME}.json"
done
