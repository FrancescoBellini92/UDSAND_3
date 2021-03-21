def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number in (0,1):
        return number

    if number < 4:
        return 1

    x = number
    while True :
        root = 0.5 * (x + (number / x))

        if (abs(root - x) < 1) :
            return round(root)

        x = root


# test case 1 -> find exact square root
print ("Pass" if  (3 == sqrt(9)) else "Fail")

#test case 2 -> find square root of 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")

#test case 3 -> find square root of 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")

#test case 4 -> find floored square root
print ("Pass" if  (5 == sqrt(27)) else "Fail")

#test case 5 -> find floored square root of decimal
print ("Pass" if  (3 == sqrt(28/3)) else "Fail")