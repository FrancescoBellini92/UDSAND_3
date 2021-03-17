# TASK 4 EXPLANATION

This task required solving the Dutch national flag problem.
Given an array containing integers that are either:
- x
- y
- z
- with x < y < z

The sorting logic can be summarized as follows:
We traverse the array and compare each value with the intermediate value (the one that should be in the middle of the sorted array).
If the value is greather or smaller, it is swapped with the value at one of the end of the array

To avoid swapping the same items back and forth, we use start and end pointers that are updated each time a swap happens.

Time complexity is O(n), space complexity is O(n) as well