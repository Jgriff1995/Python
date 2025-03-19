from typing import List
"""
DONE 3/18/2025
"""

def singleNumber(nums: List[int]) -> int:

    a_map = {}
    singled = 0

    for num in nums:
        if num in a_map:
            a_map[num] += 1
        else:
            a_map[num] = 1

    for key, value in a_map.items():
        if value == 1:
            singled = key
    return singled


print(singleNumber([2, 2, 3, 2]))
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))
