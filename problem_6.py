import random, sys

def get_min_max(interger_list):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(interger_list) == 0:
        return -1

    min = sys.maxsize
    max = - sys.maxsize -1
    for number in interger_list:
        min = min if min < number else number
        max = max if max > number else number
    return (min, max)


# test case 1 -> list containing 0 - 9
l = [i for i in range(0, 10)]
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# test case 2 -> emtpy list
l = []
print ("Pass" if (-1 == get_min_max(l)) else "Fail")

# test case 3 -> list containing one number
l = [1]
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

# test case 4 -> list containing same numbers
l = [2, 2, 2]
print ("Pass" if ((2, 2) == get_min_max(l)) else "Fail")