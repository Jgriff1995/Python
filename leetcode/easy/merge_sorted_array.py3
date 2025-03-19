# Date: 03/04/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Time: 10 minutes

def merge(nums1, m, nums2, n):
    """
    Merges two sorted arrays `nums1` and `nums2` into `nums1` in-place.

    Time Complexity: O((m + n) log(m + n)) - Sorting the combined array dominates the time complexity.
    Space Complexity: O(1) - Sorting is done in-place, and no additional space is used.

    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # Replace the extra zeros in nums1 with elements from nums2
    for i in range(m, len(nums1)):
        nums1[i] = nums2[i - m]

    # Sort the combined array
    nums1.sort()
    print("Merged array (merge function):", nums1)


def betterMerge(nums1, m, nums2, n):
    """
    Merges two sorted arrays `nums1` and `nums2` into `nums1` in-place.
    This is a slightly optimized version of the `merge` function.

    Time Complexity: O((m + n) log(m + n)) - Sorting the combined array dominates the time complexity.
    Space Complexity: O(1) - Sorting is done in-place, and no additional space is used.

    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # Replace the extra zeros in nums1 with elements from nums2
    for j in range(n):
        nums1[m + j] = nums2[j]

    # Sort the combined array
    nums1.sort()
    print("Merged array (betterMerge function):", nums1)


# Test cases with elegant printing
def test_merge_functions():
    test_cases = [
        # Test case 1: Basic example
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        # Test case 2: nums1 has no elements (m = 0)
        ([0, 0, 0], 0, [1, 2, 3], 3),
        # Test case 3: nums2 has no elements (n = 0)
        ([1, 2, 3], 3, [], 0),
        # Test case 4: nums1 and nums2 have the same elements
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),
        # Test case 5: nums1 has more elements than nums2
        ([1, 3, 5, 0, 0], 3, [2, 4], 2),
        # Test case 6: nums2 has more elements than nums1
        ([2, 0, 0, 0], 1, [1, 3, 4], 3),
    ]

    for nums1, m, nums2, n in test_cases:
        print("\nTest case:")
        print(f"nums1 = {nums1}, m = {m}")
        print(f"nums2 = {nums2}, n = {n}")

        # Create copies of nums1 and nums2 to avoid modifying the original lists
        nums1_copy1 = nums1.copy()
        nums1_copy2 = nums1.copy()

        # Test the merge function
        print("Testing merge function:")
        merge(nums1_copy1, m, nums2, n)

        # Test the betterMerge function
        print("Testing betterMerge function:")
        betterMerge(nums1_copy2, m, nums2, n)


# Run the test cases
test_merge_functions()
