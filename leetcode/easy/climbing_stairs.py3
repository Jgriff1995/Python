# Date: 03/04/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/climbing-stairs/description/
# Time: S: 30 mins

def climbStairs(n):
    """
    Calculates the number of distinct ways to climb to the top of a staircase with `n` steps.
    Each time you can either climb 1 or 2 steps. The solution uses a Fibonacci-like approach.

    Time Complexity: O(n) - We iterate from 3 to n once.
    Space Complexity: O(1) - We use only two variables (`a` and `b`) to store intermediate results.

    :type n: int
    :rtype: int
    """

    # Base cases:
    # If there is only 1 step, there is only 1 way to climb it.
    if n == 1:
        return 1
    # If there are 2 steps, there are 2 ways to climb it: (1+1) or (2).
    if n == 2:
        return 2

    # Initialize variables to store the number of ways to climb the stairs.
    # `a` represents the number of ways to reach the (i-2)th step.
    # `b` represents the number of ways to reach the (i-1)th step.
    a, b = 1, 2

    # Iterate from step 3 to step n.
    # At each step, update the number of ways to reach the current step
    # by summing the ways to reach the previous two steps.
    for _ in range(3, n + 1):
        a, b = b, a + b  # Update `a` and `b` for the next step.
        # Print intermediate values for debugging.
        print(f"Step {_}: a = {a}, b = {b}")

    # `b` now contains the number of ways to reach the nth step.
    return b


# Test cases with elegant printing
def test_climbStairs():
    test_cases = [
        1,  # Base case: 1 step
        2,  # Base case: 2 steps
        3,  # 3 steps: (1+1+1), (1+2), (2+1)
        4,  # 4 steps: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
        5,  # 5 steps: 8 ways
        10,  # 10 steps: 89 ways
    ]

    for n in test_cases:
        print(f"Test case: n = {n}")
        result = climbStairs(n)
        print(f"Number of distinct ways to climb {n} steps: {result}\n")


# Run the test cases
test_climbStairs()
