# Reference Graph

## Requirements

This requires the [anystyle.io](https://anystyle.io/) parser to retrieve references from pdf files.
Python3
Zotero
Obsidian

## Usage

### With Makefile:

```sh
make all STORAGE_PATH=<path to Zotero/storage folder>
```

Or simply:

```sh
make
```

Which will use `~/Zotero/storage` as `STORAGE_PATH` by default.

### Without Makefile:

First run:

```sh
bash extract_refs.sh <path to Zotero/storage folder>
```

It retrieve the list of pdf files in Zotero and puts it on a file called `pdfs.txt`, these files' references are then extracted by `anystyle` and put on a folder called `refs`.

After that, run:

```sh
python3 build_graph.py
```

Which will read the references and format them in a common format. 

>> This is hardcoded and references are not always well formatted so the results are not completely right.

Finally placing them in `Markdown` files inside the folder `graph` with the name of the document they were referenced by and in `Obsidian` links.

#### Checking which references are more common:

```sh
python3 build_graph.py | sort | uniq -c | sort -h
```

### Visualization

Open the folder `graph` as a vault in `Obsidian` and check the graph!

