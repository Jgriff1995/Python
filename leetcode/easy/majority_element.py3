# Date: 3/04/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/majority-element
# Difficulty: Easy
# Time Spent: 30 mins

def majorityElement(nums):
    """
    Finds the majority element in an array, which appears more than n/2 times.

    Time Complexity: O(n) - We iterate through the array once to count occurrences.
    Space Complexity: O(n) - We use a dictionary to store the count of each element.

    :type nums: List[int]
    :rtype: int
    """
    count_dict = {}  # Dictionary to store the count of each element

    # Iterate through the array and count occurrences of each element
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    # Find the key with the maximum value in the dictionary
    majority = max(count_dict, key=count_dict.get)

    return majority


# Test cases with elegant printing
def test_majorityElement():
    test_cases = [
        # Test case 1: Basic example
        [3, 2, 3],
        # Test case 2: Majority element at the end
        [3, 3, 4],
        # Test case 3: Majority element with multiple occurrences
        [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2],
        # Test case 4: Single element
        [2],
        # Test case 5: All elements are the same
        [4, 4, 4, 4],
        # Test case 6: Large array with a clear majority
        [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7],
    ]

    for nums in test_cases:
        print("\nTest case:")
        print(f"Input array: {nums}")
        result = majorityElement(nums)
        print(f"Majority element: {result}")


# Run the test cases
test_majorityElement()
