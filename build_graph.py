import json
import os


def main():
    files = os.listdir("refs")

    ref_graph: dict[str, list[str]] = {}

    for file in files:
        filename = file[:len(file)-5]
        ref_graph[filename] = []

        with open(f"refs/{file}", 'r') as readfile:
            for line in readfile:
                data = json.loads(line)
                title = data['title']
                date = data['date']
                authors = data['author']
                if authors is not None:
                    list(filter(lambda x: x is not None, authors))

                typ = data['type']

                family_list = []
                if authors is not None:
                    family_list = list(
                        filter(lambda x: 'family' in x, authors))

                author_name = None
                if authors is None or len(authors) == 0:
                    author_name = None
                elif 'family' not in authors[0]:
                    author_name = f"{'unknown' if typ is None else typ}:"
                    if 'given' in authors[0]:
                        author_name += authors[0]['given']
                    else:
                        author_name += 'unknown'
                elif 'family' in authors[0] and title is None:
                    continue
                elif len(family_list) == 0:
                    author_name = None
                elif len(family_list) > 2:
                    author_name = family_list[0]['family'] + " et al"
                else:
                    author_name = " and ".join(
                        map(lambda x: x['family'], family_list)
                    )

                if title is None:
                    continue

                refname = " - ".join(
                    filter(lambda x: x is not None, [
                        author_name, date, title]))

                print(f"{refname}")
                ref_graph[filename].append(refname)

    for key, value in ref_graph.items():
        with open(f"graph/{key}.md", "w") as new_file:
            new_file.write("\n".join(map(lambda x: f"[[{x}]]", value)))


if __name__ == "__main__":
    main()
