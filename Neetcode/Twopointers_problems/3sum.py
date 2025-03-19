from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    print(nums)
    result = []

    left, right = 0, len(nums) - 1

    # while left < right:

    # 1. Need to consider a third pointer (i) that will iterate through array
    # total_sum = 0

    # for i in range(len(nums)):

    # 2. For each i, use two pointers (left and right) to find pairs that sum to -nums[i]
    # 3. Skip duplicates to avoid duplicate triplets
    # 4. If sum > target: decrease right
    # 5. If sum < target: increase left
    # 6. If sum == target: add to result and move both pointers
    # 7. Handle edge cases (empty array, array length < 3)

    return []


threeSum([-1, 0, 1, 2, -1, -4])
