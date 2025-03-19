# Date: 03/04/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Time: 1hr

# My 1st approach - 197/219 test cases passed (Fails with Large inputs)


def maxProfit(prices: list[int]) -> int:
    """
    Calculates the maximum profit by buying and selling a stock on the best days.
    This is a brute-force approach that checks all possible buy-sell pairs.

    Time Complexity: O(n^2) - We use nested loops to compare each pair of days.
    Space Complexity: O(1) - We use only a few variables to store intermediate results.

    :type prices: List[int]
    :rtype: int
    """
    currentProfit = 0
    profit = 0

    # Simulate profit for each day using i as buy day and all possible n days as sell days
    for i in range(len(prices)):
        remaining_days = prices[i + 1:]
        for j in range(len(remaining_days)):
            currentProfit = remaining_days[j] - prices[i]
            if currentProfit > profit and currentProfit >= 0:
                profit = currentProfit

    return profit

# 2nd Approach - Passes all Test Cases


def maxProfit2(prices: list[int]) -> int:
    """
    Calculates the maximum profit by buying and selling a stock on the best days.
    This is an optimized approach that iterates through the array once.

    Time Complexity: O(n) - We iterate through the array once.
    Space Complexity: O(1) - We use only a few variables to store intermediate results.

    :type prices: List[int]
    :rtype: int
    """
    buy_price = prices[0]  # Initialize buy price to the first day's price
    profit = 0  # Initialize profit to 0

    # Iterate through the prices starting from the second day
    for p in prices[1:]:
        if buy_price > p:
            # Update buy price if the current price is lower
            buy_price = p
        # Update profit if selling at the current price yields a higher profit
        profit = max(profit, p - buy_price)

    return profit


# Test cases with elegant printing
def test_maxProfit_functions():
    test_cases = [
        # Test case 1: Basic example
        [7, 1, 5, 3, 6, 4],
        # Test case 2: Prices are decreasing
        [7, 6, 4, 3, 1],
        # Test case 3: Only two days, increasing prices
        [1, 2],
        # Test case 4: Prices decrease and then increase
        [2, 1, 4],
        # Test case 5: Single day
        [5],
        # Test case 6: Prices are the same every day
        [3, 3, 3, 3, 3],
        # Test case 7: Large array with increasing prices
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        # Test case 8: Large array with decreasing prices
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        # Test case 9: Large array with random prices
        [3, 8, 1, 4, 7, 2, 9, 5, 6, 10],
    ]

    for prices in test_cases:
        print("\nTest case:")
        print(f"Prices: {prices}")

        # Test maxProfit function
        result1 = maxProfit(prices)
        print(f"Result (maxProfit function): {result1}")

        # Test maxProfit2 function
        result2 = maxProfit2(prices)
        print(f"Result (maxProfit2 function): {result2}")


# Run the test cases
test_maxProfit_functions()
