from typing import List

# Done 3/18/2025

def rotate(nums: List[int], k: int) -> None:

    # Two pointer approach
    n = len(nums)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    for i in range(n):
        nums[i] = rotated[i]

    print(nums)


example_input = [-1, -100, 3, 99]
example_k = 2
rotate(example_input, example_k)
