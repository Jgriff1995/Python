from typing import List

"""
* Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

* A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
* The elements do not have to be consecutive in the original array.

! You must write an algorithm that runs in O(n) time.

"""


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)  # Convert to set for O(1) lookups
    longest = 0

    for num in num_set:
        # Only start checking sequences from the smallest number in the sequence
        if num - 1 not in num_set:
            # This will be the start of a sequence
            current_num = num
            current_streak = 1  # Initialize streak counter
            # Check if next consecutive number exists
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            # set longest to the max of longest and current_streak
            longest = max(longest, current_streak)
            # reset current_streak
            current_streak = 0

    return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
