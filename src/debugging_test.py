"""
debugging_test_max_subarray.py

This script is designed to test your debugging capabilities.

The function 'max_subarray_sum' below is intended to return the maximum possible sum
of any contiguous subarray within the input list of integers. However, there's a bug
that you need to fix.

Use the built-in tests at the bottom of this file to verify that your fix is correct.
"""

def max_subarray_sum(nums):
    """
    Returns the largest sum of any contiguous subarray in nums.
    For example, max_subarray_sum([1, -1, 2, 3]) should return 5,
    because the subarray [2, 3] has the sum 5.
    """

    current_sum = 0
    max_sum = 0 

    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum


if __name__ == "__main__":
    # Test cases: each tuple is (input_list, expected_output)
    test_cases = [
        ([1, 2, 3], 6),               
        ([1, -1, 2, -1, 3], 5),       
        ([-2, -3, -1], -1),           
        ([0, 0, 0], 0),               
        ([2, -1, 2, 3, 4, -5, 4], 10) 
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = max_subarray_sum(arr)
        print(f"Test {i}: Input = {arr}")
        print(f"Expected = {expected}, Got = {result}")
        if result == expected:
            print("Success\n")
        else:
            print("Failure\n")