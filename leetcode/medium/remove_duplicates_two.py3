# Date: 03/04/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# Difficulty: Medium
# Time: 1hr

# Correct Approach - 169/169 Test cases working
def removeDuplicates(nums):
    """
    Removes duplicates from a sorted array in-place, allowing at most 2 duplicates of each element.
    Returns the length of the modified array.

    Time Complexity: O(n) - We iterate through the array once.
    Space Complexity: O(1) - We modify the array in-place and use only a few extra variables.

    :type nums: List[int]
    :rtype: int
    """
    # Edge case:
    if not nums:
        return 0

    count = 0  # Tracks the number of duplicates for the current element
    current = 1  # Pointer for the position to place the next valid element

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            # If the current element is different from the previous one, reset the count
            count = 0
            nums[current] = nums[i]
            current += 1
        else:
            # If the current element is the same as the previous one, increment the count
            count += 1
            if count <= 1:
                # Allow at most 2 duplicates
                nums[current] = nums[i]
                current += 1

    return current


# Test cases with elegant printing
def test_removeDuplicates():
    test_cases = [
        # Test case 1: Basic example
        [1, 1, 2, 2, 2, 3, 3, 3],
        # Test case 2: Multiple duplicates
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        # Test case 3: Longer array with multiple duplicates
        [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6],
        # Test case 4: No duplicates
        [1, 2, 3, 4, 5],
        # Test case 5: All elements are the same
        [2, 2, 2, 2, 2],
        # Test case 6: Empty array
        [],
    ]

    for nums in test_cases:
        print("\nTest case:")
        print(f"Input array: {nums}")
        result_length = removeDuplicates(nums)
        print(f"Modified array: {nums[:result_length]}")
        print(f"Length of modified array: {result_length}")


# Old Work - working for 69/169 test cases
def removeDuplicatesOld(nums):
    """
    Old implementation of removing duplicates. This version is less efficient and only works for 69/169 test cases.

    Time Complexity: O(n^2) - Due to nested loops and sorting.
    Space Complexity: O(1) - Modifies the array in-place but uses inefficient logic.

    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    maxValue = max(nums)
    initialMaxValue = max(nums)

    # Start with first number in list
    for i in range(len(nums)):
        count = 0
        currNum = nums[i]
        lastIndex = 0

        # Iterate over rest of list, adding the #'s to a count variable
        for j in range(len(nums)):
            # If count is already over 2, we have too many
            if count > 2:
                break  # Break out of inner loop
            # Else, add to count and keep track of the lastIndex j
            if nums[j] == currNum:
                count += 1
                lastIndex = j

        if count > 2:
            nums[lastIndex] = (max(nums) / (i + 1)) + 10
            if maxValue < nums[lastIndex] and i != len(nums):
                maxValue = nums[lastIndex]
            nums.sort()

    initialMaxIndex = find_last_index(nums, initialMaxValue)
    nums = nums[0:initialMaxIndex + 1]

    return len(nums)


def find_last_index(list1, num):
    """
    Helper function to find the last index of a given number in a list.

    :type list1: List[int]
    :type num: int
    :rtype: int
    """
    for i in reversed(range(len(list1))):
        if list1[i] == num:
            return i
    return -1


# Test cases for the old implementation
def test_removeDuplicatesOld():
    test_cases = [
        # Test case 1: Basic example
        [1, 1, 2, 2, 2, 3, 3, 3],
        # Test case 2: Multiple duplicates
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        # Test case 3: Longer array with multiple duplicates
        [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6],
    ]

    for nums in test_cases:
        print("\nTest case (Old Implementation):")
        print(f"Input array: {nums}")
        result_length = removeDuplicatesOld(nums)
        print(f"Modified array: {nums[:result_length]}")
        print(f"Length of modified array: {result_length}")


# Run the test cases
print("Testing removeDuplicates function:")
test_removeDuplicates()

print("\nTesting removeDuplicatesOld function:")
test_removeDuplicatesOld()
