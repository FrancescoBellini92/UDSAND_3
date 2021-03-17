# TASK 5 EXPLANATION

This task required using a Trie for making an autocomplete automata.

Regarding time complexity:
- we consider time complexity in case of traversal for finding the suffixes associated to the given prefix
- given n as the size of the input (n being the lengh of the prefix),
- time complexity is O(n) as each of the character requires traversing a node.

Regarding space complexity:
- we consider space complexity not regarding the traversal per se but the persitence in memory of all words
- each char creates a new node, so given n as the number of words to store and m as the length of the longest word (worst case)
- space complexity is O(n * m)