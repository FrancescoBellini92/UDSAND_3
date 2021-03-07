def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low_i = 0
    pivot_i = 0
    high_i = len(input_list) - 1
    mid_val = 1

    while pivot_i <= high_i:
        if input_list[pivot_i] < mid_val:
            input_list[low_i], input_list[pivot_i] = input_list[pivot_i], input_list[low_i]
            low_i += 1
            pivot_i += 1
        elif input_list[pivot_i] > mid_val:
            input_list[pivot_i], input_list[high_i] = input_list[high_i], input_list[pivot_i]
            high_i -= 1
        else:
            pivot_i += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# test 1 -> sort unsortd array
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# test 2 -> sort reverse-sorted array
test_function([2, 2, 2, 1, 1, 1, 0, 0, 0])

# test 3 -> sort already-sorted array
test_function([0, 0, 0, 1, 1, 1, 2, 2, 2])

# test 4 -> sort empty array
test_function([])
