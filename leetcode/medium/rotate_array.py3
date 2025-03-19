# Date: 3/04/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium
# Time Spent: 1 hr

# First implementation, worked for 1/3 of test cases - WRONG


def rotate(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps using a brute-force approach.

    Time Complexity: O(n * k) - In the worst case, we perform `k` insertions, each taking O(n) time.
    Space Complexity: O(1) - We modify the array in-place.

    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    while k > 0:
        nums.insert(0, nums.pop())  # Move the last element to the front
        k -= 1

# Second Implementation, worked for 67/68 cases - WRONG


def rotate2(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps using a slicing approach.

    Time Complexity: O(n) - Slicing and concatenation take linear time.
    Space Complexity: O(n) - We create a new list `nums_split` of size `k`.

    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 2:
        # Handle edge case for arrays of length 2
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return

    k = k % len(nums)  # Handle cases where k > len(nums)
    nums_split = nums[-k:]  # Extract the last `k` elements
    nums[:] = nums[:-k]  # Remove the last `k` elements
    nums[:] = nums_split + nums  # Concatenate the two parts

# Third Implementation: Passes all test cases


def rotate3(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps using an auxiliary array.

    Time Complexity: O(n) - We iterate through the array twice.
    Space Complexity: O(n) - We use an auxiliary array of size `n`.

    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n  # Handle cases where k > n
    rotated = [0] * n  # Auxiliary array to store the rotated elements

    # Fill the auxiliary array with rotated elements
    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    # Copy the rotated elements back to the original array
    for i in range(n):
        nums[i] = rotated[i]


# Test cases with elegant printing
def test_rotate_functions():
    test_cases = [
        # Test case 1: Basic example
        ([-1, -100, 3, 99], 2),
        # Test case 2: Small array with k > len(nums)
        ([1, 2], 3),
        # Test case 3: Large array with k > len(nums)
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
         50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], 192),
        # Test case 4: Single element
        ([5], 10),
        # Test case 5: All elements are the same
        ([2, 2, 2, 2], 3),
        # Test case 6: k = 0 (no rotation)
        ([1, 2, 3, 4, 5], 0),
    ]

    for nums, k in test_cases:
        print("\nTest case:")
        print(f"Input array: {nums}")
        print(f"k: {k}")

        # Test rotate function
        nums_copy1 = nums.copy()
        rotate(nums_copy1, k)
        print("Result (rotate function):", nums_copy1)

        # Test rotate2 function
        nums_copy2 = nums.copy()
        rotate2(nums_copy2, k)
        print("Result (rotate2 function):", nums_copy2)

        # Test rotate3 function
        nums_copy3 = nums.copy()
        rotate3(nums_copy3, k)
        print("Result (rotate3 function):", nums_copy3)


# Run the test cases
test_rotate_functions()
