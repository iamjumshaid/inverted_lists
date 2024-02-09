import re
import argparse
from typing import Dict, List

class InvertedListBuilder:

    def __init__(self) -> None:
        self.inverted_list: Dict[str, List[int]] = {}

    def read_from_file(self, file_name: str) -> Dict[str, List[int]]:
        """
        >>> sorted(InvertedListBuilder().read_from_file('example.tsv').items())
        [('a', [1, 2]), ('film', [2]), ('movie', [1, 3])]
        """
        with open(file_name, 'r') as file:
            doc_id = 0
            for line in file:
                doc_id += 1
                title, desc, _ = line.split('\t', 2)
                words = re.findall(r'[A-Za-z]+', desc)
                for word in words:
                    word = word.lower()
                    if word not in self.inverted_list:
                        self.inverted_list[word] = []
                    if doc_id not in self.inverted_list[word]:
                        self.inverted_list[word].append(doc_id)
        return self.inverted_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build inverted index from a file.")
    parser.add_argument("file_name", type=str, help="Enter the filename string.")
    args = parser.parse_args()

    builder = InvertedListBuilder()
    inverted_list = builder.read_from_file(file_name=args.file_name)
    for word in inverted_list:
        print(f"{word}: {len(inverted_list[word])}")
