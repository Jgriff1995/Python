# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Time Spent: 1hr+

# LeetCode implementation - Inspired by "TheSubtleOne"'s solution.
def romanToInt(s):
    """
    Converts a Roman numeral string to an integer.

    :type s: str - Input string representing a Roman numeral.
    :rtype: int - The integer value of the Roman numeral.

    Time Complexity: O(n) - Linear time complexity, where n is the length of the input string.
    Space Complexity: O(1) - Constant space, as the dictionary size is fixed.
    """

    # Dictionary to map Roman numeral symbols to their corresponding integer values.
    roman_to_int = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

    result = 0  # Variable to store the cumulative result.

    # Iterate through each character in the input string.
    for i in range(len(s)):
        # Check if the current symbol is smaller than the next symbol (subtractive case).
        if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            # Subtract the current symbol's value.
            result -= roman_to_int[s[i]]
        else:
            result += roman_to_int[s[i]]  # Add the current symbol's value.
    return result


# Old implementation - My original submission, optimized once.
def romanToIntOld(s):
    """
    Converts a Roman numeral string to an integer.

    :type s: str - Input string representing a Roman numeral.
    :rtype: int - The integer value of the Roman numeral.

    Time Complexity: O(n) - Linear time complexity, where n is the length of the input string.
    Space Complexity: O(1) - Constant space, as the dictionary sizes are fixed.
    """

    # Dictionary to map Roman numeral symbols to their corresponding integer values.
    roman_to_int = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

    # Dictionary to handle subtractive combinations (e.g., IV, IX, XL, etc.).
    roman_sub = {"IV": 4,
                 "IX": 9,
                 "XL": 40,
                 "XC": 90,
                 "CD": 400,
                 "CM": 900}

    digits = 0  # Variable to store the cumulative sum of the Roman numeral.
    i = 0  # Index to iterate through the string.

    # Edge case: If the input is a single Roman numeral (e.g., "I").
    if len(s) == 1:
        return roman_to_int.get(s)

    # Iterate through the Roman numeral string.
    while i < len(s):
        # Temporary variable to store the current and next character (for subtractive cases).
        temp = ""
        for symbol, int_value in roman_to_int.items():
            if s[i] == symbol:
                # Check if the current and next characters form a subtractive combination.
                # Ensure we don't go out of bounds.
                if i >= 0 and i < len(s) - 1:
                    temp = s[i] + s[i+1]
                    # Check if the combination is in the subtractive dictionary.
                    if roman_sub.get(temp) is not None:
                        # Add the subtractive value.
                        digits += roman_sub.get(temp, 0)
                        # Move the index forward by 2 (skip the next character).
                        i += 2
                        break  # Exit the inner loop.
                # Add the current symbol's value.
                digits += roman_to_int.get(symbol, 0)
                i += 1  # Move the index forward by 1.
                break  # Exit the inner loop.
    return digits


# Test cases to validate the new implementation.
print("New Implementation Test Cases: ")
print(romanToInt("III"))      # Output: 3
print(romanToInt("IV"))       # Output: 4
print(romanToInt("VI"))       # Output: 6
print(romanToInt("MCMXCIV"))  # Output: 1994
print(romanToInt("I"))        # Output: 1
print(romanToInt("X"))        # Output: 10
print(romanToInt("LVIII"))    # Output: 58

print()

# Test cases to validate the old implementation.
print("Old Implementation Test Cases: ")
print(romanToIntOld("III"))      # Output: 3
print(romanToIntOld("IV"))       # Output: 4
print(romanToIntOld("VI"))       # Output: 6
print(romanToIntOld("MCMXCIV"))  # Output: 1994
print(romanToIntOld("I"))        # Output: 1
print(romanToIntOld("X"))        # Output: 10
print(romanToIntOld("LVIII"))    # Output: 58
