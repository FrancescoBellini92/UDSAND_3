
"""
Finding suffixes with a trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings.
Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
"""

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    @property
    def suffixes(self):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []

        for child in self.children:
            child_node = self.children[child]
            if child_node.is_word:
                suffixes.append(child)

            for suffix in child_node.suffixes:
                suffix = child + suffix
                suffixes.append(suffix)

        return suffixes

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node


def find_suffixes(prefix, trie):
    if prefix != '':
        prefixNode = trie.find(prefix)
        if prefixNode:
            print('------------\nSuffixes found:')
            print('\n'.join(prefixNode.suffixes))
            print('------------\n')
        else:
            print(prefix + " not found")
    else:
        print('')


def main():
    trie = Trie()
    words = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in words:
        trie.insert(word)

    print('----------')
    while True:
        prefix_to_find = input('Prefix to find (press q to quit): ')
        if prefix_to_find == 'q':
            break
        find_suffixes(prefix_to_find, trie)


if __name__ == '__main__':
    main()
