from typing import List

# https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150


def maxPoints(points: List[List[int]]) -> int:
    """ """

    print(f"Original List: {points}")

    # First sort the inputs
    input_sorted = sorted(points)

    print(f"Sorted List: {input_sorted}")


input_1 = [[1, 1], [2, 2], [3, 3]]
input_2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

maxPoints(input_1)
maxPoints(input_2)
