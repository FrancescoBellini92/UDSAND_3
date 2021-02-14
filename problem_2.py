
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    pivot = find_pivot(input_list, 0, len(input_list) - 1)
    if pivot > -1:
        target_in_left = find_target(input_list, 0, pivot, number)
        target_in_right = find_target(input_list,pivot, len(input_list) - 1, number)
        return max(target_in_left, target_in_right)
    else: # not rotated
        return find_target(input_list, 0, len(input_list) - 1, number)

def find_pivot(arr, left_i, right_i):
        indexes_out_of_boundaries = left_i >= right_i or right_i < left_i
        if indexes_out_of_boundaries:
            return -1

        middle_i = (left_i + right_i) // 2
        is_pivot =  arr[middle_i + 1] < arr[middle_i]
        if is_pivot:
            return middle_i

        pivot_in_left = find_pivot(arr, left_i, middle_i - 1)
        pivot_in_right = find_pivot(arr, middle_i + 1, right_i)
        return max(pivot_in_left, pivot_in_right)

def find_target(arr, left_i, right_i, target):
        indexes_out_of_boundaries = left_i > right_i or right_i < left_i
        if indexes_out_of_boundaries:
            return -1

        middle_i = (left_i + right_i) // 2
        is_target =  arr[middle_i] == target
        if is_target:
            return middle_i

        pivot_in_left = find_target(arr, left_i, middle_i - 1, target)
        pivot_in_right = find_target(arr, middle_i + 1, right_i, target)
        return max(pivot_in_left, pivot_in_right)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# test 1 -> find number in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])

# test 2 -> find number not in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11])

# test 3 -> find number in empty array
test_function([[], 1])

# test 4 -> find number in sorted array asymmentrically rotated
test_function([[10, 1, 2, 3, 4], 3])

# test 6 -> find number in sorted array not rotated
test_function([[1, 2, 3, 4, 5], 3])

# test 7 -> find number at end
test_function([[1, 2, 3, 4, 5], 5])

# test 7 -> find number at start
test_function([[1, 2, 3, 4, 5], 1])
