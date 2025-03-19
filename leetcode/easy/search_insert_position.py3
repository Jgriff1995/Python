# Date: 3/03/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/search-insert-position/
# Time: 45 mins

# My approach - organic
def searchInsert(nums, target):
    """
    Finds the index where `target` should be inserted in the sorted list `nums` to maintain order.
    If `target` is already in `nums`, returns its index.

    :type nums: List[int] - A sorted list of integers.
    :type target: int - The target value to search or insert.
    :rtype: int - The index where `target` is or should be inserted.

    Time Complexity: O(log n) - Binary search is used to find the index.
    Space Complexity: O(1) - Constant space, as no additional data structures are used.
    """

    # First, check if the target is already in the list.
    for i in range(len(nums)):
        if nums[i] == target:
            return i  # Return the index if the target is found.

    # If the target is not found, add it to the list and sort the list.
    nums.append(target)
    nums.sort()

    # Use binary search to find the index of the target in the sorted list.
    return binary_search(nums, target)


# Helper Function for searchInsert
def binary_search(nums, target):
    """
    Helper function to perform binary search on a sorted list.

    :type nums: List[int] - A sorted list of integers.
    :type target: int - The target value to search for.
    :rtype: int - The index of the target in the list, or -1 if not found.
    """

    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2  # Calculate the middle index.

        # If the target is greater than the middle element, ignore the left half.
        if nums[mid] < target:
            low = mid + 1

        # If the target is smaller than the middle element, ignore the right half.
        elif nums[mid] > target:
            high = mid - 1

        # If the target is equal to the middle element, return the index.
        else:
            return mid

    # If the target is not found, return -1.
    return -1


# Optimized approach - from leetcode solutions
def searchInsertOptimized(nums, target):
    """
    Finds the index where `target` should be inserted in the sorted list `nums` to maintain order.
    If `target` is already in `nums`, returns its index.

    :type nums: List[int] - A sorted list of integers.
    :type target: int - The target value to search or insert.
    :rtype: int - The index where `target` is or should be inserted.

    Time Complexity: O(log n) - Binary search is used to find the index.
    Space Complexity: O(1) - Constant space, as no additional data structures are used.
    """

    # Initialize pointers for binary search.
    left = 0  # Left pointer.
    right = len(nums) - 1  # Right pointer.

    # Perform binary search.
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index.

        # If the middle element is less than the target, search the right half.
        if nums[mid] < target:
            left = mid + 1
        # If the middle element is greater than the target, search the left half.
        elif nums[mid] > target:
            right = mid - 1
        else:  # If the middle element is equal to the target, return the index.
            return mid

    # If the target is not found, return the insertion position (left pointer).
    return left


# Test cases to validate the function.
print("Test Case 1: [1, 3, 4, 6], 1: Index: ",
      searchInsert([1, 3, 4, 6], 1))  # Output: 0
print("Test Case 2: [1, 3, 4, 6], 3: Index: ",
      searchInsert([1, 3, 4, 6], 3))  # Output: 1
print("Test Case 3: [1, 3, 4, 6], 4: Index: ",
      searchInsert([1, 3, 4, 6], 4))  # Output: 2
print("Test Case 4: [1, 3, 4, 6], 7: Index: ",
      searchInsert([1, 3, 4, 6], 7))  # Output: 4
print("Test Case 5: [1, 3, 5, 6], 2: Index: ",
      searchInsert([1, 3, 5, 6], 2))  # Output: 1
print("Test Case 6: [1, 3, 5, 6], 0: Index: ",
      searchInsert([1, 3, 5, 6], 0))  # Output: 0
# Output: 0 (edge case: empty list)
print("Test Case 7: [], 5: Index: ", searchInsert([], 5))
print("Test Case 8: [1, 3, 5, 6], 5: Index: ",
      searchInsert([1, 3, 5, 6], 5))  # Output: 2
print("Test Case 9: [1, 3, 5, 6], 6: Index: ",
      searchInsert([1, 3, 5, 6], 6))  # Output: 3
print("Test Case 10: [1, 3, 5, 6], 4: Index: ",
      searchInsert([1, 3, 5, 6], 4))  # Output: 2

print()

# Test cases to validate the function.
print("Test Case 1: [1, 3, 5, 6], 5: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 5))  # Output: 2
print("Test Case 2: [1, 3, 5, 6], 2: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 2))  # Output: 1
print("Test Case 3: [1, 3, 5, 6], 7: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 7))  # Output: 4
print("Test Case 4: [1, 3, 5, 6], 0: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 0))  # Output: 0
# Output: 0 (edge case: empty list)
print("Test Case 5: [], 5: Index: ", searchInsertOptimized([], 5))
print("Test Case 6: [1, 3, 5, 6], 6: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 6))  # Output: 3
print("Test Case 7: [1, 3, 5, 6], 4: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 4))  # Output: 2
print("Test Case 8: [1, 3, 5, 6], 1: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 1))  # Output: 0
print("Test Case 9: [1, 3, 5, 6], 3: Index: ",
      searchInsertOptimized([1, 3, 5, 6], 3))  # Output: 1
print("Test Case 10: [2, 4, 6, 8], 5: Index: ",
      searchInsertOptimized([2, 4, 6, 8], 5))  # Output: 2
