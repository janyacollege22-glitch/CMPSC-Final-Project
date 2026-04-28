# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables.
# Use recursion, otherwise no credit will be given
# No helper functions allowed!

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    ## YOUR CODE STARTS HERE
    if num == 1: # any number to the power of 0 is 1, so we can return True if num is 1
        return True # if num is 1, then it is a power of base (base^0 = 1)
    elif num < 1 or base <= 1:# if num is less than 1, then it cannot be a power of base (since powers of positive integers are always greater than or equal to 1). Also, if base is less than or equal to 1, then it cannot be a power of any number (since powers of 1 are always 1, and powers of numbers less than 1 are always less than 1).
        return False
    else:
        return is_power_of(base, num // base) if num % base == 0 else False# if num is divisible by base, then we can check if num // base is a power of base. If num is not divisible by base, then it cannot be a power of base, so we return False.
    
    pass




def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
	"""
    ## YOUR CODE STARTS HERE
    i = 0
    result = []
    while i < len(a_list):
        if a_list[i] < 0: # if the current element is negative, we need to delete it and the next element (if it exists)
            i += abs(a_list[i]) # skip the next element as well if its the abs value of the current element 
        else:
            result.append(a_list[i]) # if the current element is not negative, we can add it to the result list
            i += 1 # move to the next element
    return result
   
    pass




def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    ## YOUR CODE STARTS HERE
    if len(num_list) == 0: # if the input list is empty, we can return an empty list
        return []
    elif len(num_list) == 1: # if the input list has only one element, we can return a list with that element
        return num_list
    else:
        right_max_list = right_max(num_list[1:]) # get the right max list for the rest of the input list
        return [max(num_list[0], right_max_list[0])] + right_max_list # compare the first element of the input list with the first element of the right max list and return a new list with the maximum of the two as the first element, followed by the rest of the right max list
    
    pass





def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    ## YOUR CODE STARTS HERE
    if num < 10: # if the input number has only one digit, we can return True (since there are no consecutive digits to compare)
        return False
    else:
        last_digit = num % 10 # get the last digit of the input number
        second_last_digit = (num // 10) % 10 # get the second last digit of the input number
        if last_digit == second_last_digit: # if the last digit is equal to the second last digit, we can check the rest of the input number
            return True # if the last digit is equal to the second last digit, we can return True (since there are consecutive digits that are equal)

        return consecutive_digits(num // 10) # if the last digit is not equal to the second last digit, we can check the rest of the input number by removing the last digit (i.e., dividing the input number by 10)
    



def only_evens(num):
    """
        >>> only_evens(4386112)
        4862
        >>> only_evens(0)
        0
        >>> only_evens(357997555531)
        0
        >>> only_evens(13847896213354889741236)
        84862488426
    """
    ## YOUR CODE STARTS HERE
    if num == 0: # if the input number is 0, we can return 0 (since there are no digits to compare)
        return 0
    else:
        last_digit = num % 10 # get the last digit of the input number
        if last_digit % 2 == 0: # if the last digit is even, we can include it in the result
            return only_evens(num // 10) * 10 + last_digit # we can multiply the result of the recursive call by 10 and add the last digit to include it in the result
        else:
            return only_evens(num // 10) # if the last digit is odd, we can simply return the result of the recursive call (i.e., remove the last digit and check the rest of the input number)
    pass



def run_tests():
    import doctest

    #- Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    #- Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function you want to test
    doctest.run_docstring_examples(only_evens, globals(), name='LAB3',verbose=True)

if __name__ == "__main__":
    run_tests()