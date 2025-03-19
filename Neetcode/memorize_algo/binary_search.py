from typing import List


def binarySearch(nums: List[int], target: int) -> int:

    left, right = 0, len(nums) - 1

    while left <= right:

        middle_index = left + (right - left) // 2

        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] < target:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
