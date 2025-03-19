from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    left, right = 0, len(numbers) - 1

    while left < right:

        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left + 1, right + 1]


print(twoSum([1, 2, 3, 4], 3))
print(twoSum([1, 2, 4, 5, 7, 9], 16))


basket = {"1": 1, "2": 3}

basket["2"] +=1

print(len(basket))
