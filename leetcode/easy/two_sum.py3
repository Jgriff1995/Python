# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Time Spent: 10 mins

def twoSum(nums, target):
    """
    Finds the indices of two numbers in the list that add up to the target.

    :type nums: List[int] - Input list of integers.
    :type target: int - The target sum.
    :rtype: List[int] - Indices of the two numbers that add up to the target. Returns an empty list if no solution exists.

    Time Complexity: O(n^2) - Nested loop iterates over all pairs of numbers in the list.
    Space Complexity: O(1) - Constant space, as only a few variables are used.
    """

    # Iterate over the list of numbers starting with nums[0].
    for i in range(len(nums)):
        # Iterate over the list of numbers starting with nums[1] to avoid using the same element twice.
        for j in range(1, len(nums)):
            # Check if the sum of nums[i] and nums[j] equals the target and ensure i and j are not the same index.
            if nums[i] + nums[j] == target and i != j:
                return [i, j]  # Return the indices of the two numbers.

    # If no solution is found, return an empty list.
    return []


# Test cases to validate the function.
print("Test Case 1: ", twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print("Test Case 2: ", twoSum([3, 2, 4], 6))  # Output: [1, 2]
print("Test Case 3: ", twoSum([3, 3], 6))  # Output: [0, 1]
print("Test Case 4: ", twoSum([1, 2, 3, 4], 10))  # Output: []
print("Test Case 5: ", twoSum([-1, -2, -3, -4], -7))  # Output: [2, 3]
print("Test Case 6: ", twoSum([0, 4, 3, 0], 0))  # Output: [0, 3]
