# TASK 3 EXPLANATION

This task required finding, in an array of integers, two integers representing the two maximum sums from the integers in the array.

The logic consisted in sorting the array (time complexity of O(n log n) and then, starting from the end, summing elements in pairs (time complexity of O(n))
Since summing integers would not result in the desired result, the two sums are first managed as strings and then converted to integers.

Time complexity is O(nlog n).
Space complexity is O(n)
