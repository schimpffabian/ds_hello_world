"""
debugging_test.py

This script is designed to test your debugging capabilities.

The function 'custom_sort' below is intended to sort a list of integers in ascending order.
However, it currently contains a bug. Your task is to fix the bug.

Use the built-in test at the bottom of this file to verify that your fix is correct.
"""

def custom_sort(lst):
    """
    Sorts a list of integers in ascending order.
    param lst: List of integers to be sorted
    return: List of integers sorted in ascending order
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


if __name__ == "__main__":
    # Minimal test
    test_list = [64, 25, 12, 22, 11]
    
    # Keep an original copy for checking
    original_list_copy = test_list.copy()
    
    # Attempt to sort
    sorted_list = custom_sort(test_list)
    
    # Check if the list is actually sorted in ascending order
    if sorted_list == sorted(original_list_copy):
        print("Success: The list is sorted correctly.")
    else:
        print("Error: The list is NOT sorted correctly.")