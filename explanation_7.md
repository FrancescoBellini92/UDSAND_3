# TASK 7 EXPLANATION

This task required using a Trie for making a router

I will describe the complexity of each method of the Node and Trie classes


# Regarding time complexity

Node:
- insert: time complexity is O(1), as it involves adding a node to an hash map

Trie:
- insert: this method requires iterating on each substring of the route, thus time complexity is O(n) (given n as the substrings of the route)
- find: this method iterates over each substring of the prefix, thus time complexity is O(n)


# Regarding space complexity

Node:
- insert: space complexity is O(1), as it involves adding a node to an hash map

Trie:
- insert: this method requires creating new nodes for potentiall each substring of the route, so space complexity is O(n)
- find: this method iterates over each substring of the route, but if we consider n as the number of substrings f the route, then space complexity is O(1), as no additional space in memory is occupied during the iteration


Overall, managing data with a trie results in space complexity of O(n * m), where n is the number of routes and m is the average number of route substrings .
