from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    """Find first and last position of target in sorted array"""

    def findBound(isFirst: bool) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    if not nums:
        return [-1, -1]

    first = findBound(True)
    if first == -1:
        return [-1, -1]
    last = findBound(False)
    return [first, last]


print(searchRange([5, 7, 7, 8, 8, 10], 8))


def searchRange2(nums: List[int], target: int) -> List[int]:
    """ """
    result = []

    if len(nums) == 0:
        return [-1, -1]

    if len(nums) == 1 and target == nums[0]:
        return [0, 0]

    left, right = 0, len(nums) - 1

    while left <= right:

        middle_index = (right + left) // 2
        print(
            f"middle index is currently: {middle_index} with a value of: {nums[middle_index]}"
        )
        if nums[middle_index] < target:
            left = middle_index + 1
        elif nums[middle_index] > target:
            right = middle_index - 1
        else:
            result.append(middle_index)
            nums.remove(target)

        if target not in nums:
            break

    if len(result) != 0:
        return sorted(result)
    else:
        return [-1, -1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
