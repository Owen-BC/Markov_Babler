from pypdf import PdfReader
import argparse
import pathlib
import os
import re 
import random

class word_dict:
    def __init__(self, word):
        self.word = word
        self.parents = {} # count of parents for each word
        self.children = {} # count of children for each word
        self.sequence = {}  # the children words that should be avoided given parent, word 
        self.randomizer = None

    # should be called to update class
    def update_word(self, parent, child):
        if parent is not None:
            self.add_parent(parent)
        else:
            pass

        if child is not None:
            self.add_child(child)
        else:
            pass

        if parent is not None and child is not None:
            self.add_sequence(parent,child)

    # strictly internal
    def add_parent(self, parent):
        current = self.parents.get(parent)
        if current is not None:
            self.parents[parent] = current + 1
        else:
            self.parents[parent] = 1

    # strictly internal
    def add_child(self, child):
        current = self.children.get(child)
        if current is not None:
            self.children[child] = current + 1
        else:
            self.children[child] = 1

    def add_sequence(self, parent, child):
        result = self.sequence.get(parent)
        if result is None:
            self.sequence[parent] = list(child)
        else:
            self.sequence[parent] = result.append(child)

    def get_parents(self):
        return list(self.parents.items())
    
    def get_children(self):
        return list(self.children.items())

    def get_all(self):
        return self.parents, self.children
    
    def get_random_child(self, parent):
        children = [x[0] for x in self.get_children()]
        print(children)
        weights = [x[1] for x in self.get_children()]
        print(weights)


        return random.choices(children,weights)
    

def main():
    parser = argparse.ArgumentParser(
                    prog='Markov_Babler',
                    description='This program is designed to be able to deterministically generate random text that ' \
                    'sounds like a particular set of input PDF\'s without repeating the original verbatum',
                    epilog='Forever open source, forever free.')
    parser.add_argument('--extract','-e', help='reletive path to a folder of pdfs to train the babbler on', required=True)
    out = parser.parse_args()
    list = os.listdir(out.extract)
    for file in list:
        if re.search( ".*pdf$", file) is not None:
            reader = PdfReader(out.extract + file)

            for index in range(len(reader.pages)):

                page = reader.pages[index]

                print(page.extract_text())


def parse_text(text, library):
    pass


if __name__ == "__main__":
    main()