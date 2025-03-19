from typing import List


def maxArea(heights: List[int]) -> int:
    max_water = 0
    start, end = 0, len(heights) - 1

    while start < end:
        result = (end - start) * min(heights[end], heights[start])
        print(result)
        max_water = max(result, max_water)
        if heights[end] < heights[start]:
            end -= 1
        else:
            start += 1
    return max_water


print(maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
print(maxArea([2, 2, 2]))
