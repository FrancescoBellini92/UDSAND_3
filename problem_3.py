def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list

    sorted_arr = merge_sort(input_list)
    sum1 = ''
    sum2 = ''
    i = len(sorted_arr) - 1
    while i >= 0:
        if i == 0:
            sum1 += str(sorted_arr[i])
        else:
            sum1 += str(sorted_arr[i])
            sum2 += str(sorted_arr[i - 1])
        i -= 2

    output = [int(sum1), int(sum2)]
    print('----\nTwo maximum sums:')
    print(input_list)
    print(output)
    return output


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle_i = len(arr) // 2
    left_arr = merge_sort(arr[:middle_i])
    right_arr = merge_sort(arr[middle_i:])

    left_i = 0
    right_i = 0
    output = []
    while left_i < len(left_arr) and right_i < len(right_arr):
        left_val = left_arr[left_i]
        right_val = right_arr[right_i]
        if left_val <= right_val:
            output.append(left_val)
            left_i += 1
        else:
            output.append(right_val)
            right_i += 1

    output += left_arr[left_i:]
    output += right_arr[right_i:]
    return output

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
# test case 1 -> summing an already sorted array
test_function([[1, 2, 3, 4, 5], [531, 42]])

# test case 2 -> summing an unsorted array
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# test case 3 -> summing an empty array
test_function([[], []])

# test case 4 -> summing a single integer array
test_function([[1], [1]])

#test case 5 -> summing an array of two integers
test_function([[1, 2], [1, 2]])

# test case 6 -> summing an array of
test_function([[1, 2, 3], [32, 1]])
