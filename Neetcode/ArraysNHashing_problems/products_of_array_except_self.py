from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result[i] = product
    return result


# print(productExceptSelf([1, 2, 4, 6]))
# print(productExceptSelf([-1, 0, 1, 2, 3]))


def productExceptSelf2(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    # Calculate postfix products
    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result


# productExceptSelf2([1, 2, 4, 6])
productExceptSelf2([-1, 0, 1, 2, 3])
