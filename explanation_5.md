# TASK 5 EXPLANATION

This task required using a Trie for making an autocomplete automata.

I will describe the complexity of each method of the Node and Trie classes


# Regarding time complexity

Node:
- insert: time complexity is O(1), as it involves adding a node to an hash map
- suffixes: this method is called recursively on each node's children, resulting in time complexity of O(n * m), with n being the number of children and m being the average lenth of suffixes.

Trie:
- insert: this method requires iterating on each character of the word to insert, thus time complexity is O(n)
- find: this method iterates over each char of the prefix, thus time complexity is O(n)
- find_suffixes: this method combines the find method of the trie with the suffixes method of the node. Given n as the length of the prefix, x as the number of suffixes and z as the average length of the suffixes, time complexity is O (n + x * z)



# Regarding space complexity

Node:
- insert: space complexity is O(1), as it involves adding a node to an hash map
- suffixes: given n as the number of suffixes and m as the average length of suffixes, space complexity is O(n * m), as we can consider the memory space occupied by the characters of the suffixes

Trie:
- insert: this method requires creating new nodes for potentiall each character of the word to insert, so space complexity is O(n)
- find: this method iterates over each char of the prefix, and if we consider n as the length of the prefix as n, then space complexity is O(1), as no additional space in memory is occupied during the iteration
- find_suffixes: this method combines the find method of the trie with the suffixes method of the node. Given n as the length of the prefix, x as the number of suffixes and z as the average length of the suffixes, time complexity is O (n + x * z)

Overall, managing data with a trie results in space complexity of O(n * m), where n is the number of words and m is the average length of these words.

