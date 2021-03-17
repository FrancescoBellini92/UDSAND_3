# TASK 7 EXPLANATION

This task required traversing a tree-like structure called Trie.

Regarding time complexity:
- we consider time complexity in case of traversal for finding the handler associated to the route of interest
- given n as the size of the input (n being the sub_strings resulting from the splitting of the route),
- time complexity is O(n) as each of the sub_string requires traversing a node and exploring its children.

Regarding space complexity:
- we consider space complexity not regarding the traversal per se but the persitence in memory of all routes
- given n as the sum of all sub_strings from the splitting of all routes
- space complexity is O(n), as each sub_string requires a node