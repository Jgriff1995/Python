from typing import List


def threeSum(nums: List[int]) -> List[int]:
    """
    Two pointer problem
    """
    # List to store resulting lists of 3 nums that add to 0
    result = []

    # Sort the input list
    nums.sort()

    for index in range(len(nums)):

        if index > 0 and nums[index] == nums[index - 1]:
            continue

        left = index + 1
        right = len(nums) - 1

        while left < right:
            total = nums[index] + nums[left] + nums[right]

            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                result.append([nums[index], nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result


print(threeSum([-2, 0, 1, 1, 2]))
