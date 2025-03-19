# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Time Spent: 7 mins

def isPalindrome(x):
    """
    Determines if an integer is a palindrome.

    :type x: int - Input integer to check.
    :rtype: bool - True if the integer is a palindrome, False otherwise.

    Time Complexity: O(n) - Where n is the number of digits in the integer.
    Space Complexity: O(n) - Additional space is used to store the string representation of the integer.
    """

    # Convert the integer to a string to easily compare characters.
    converted = str(x)

    # Iterate over the string representation of the integer.
    for i in range(len(converted)):
        # Compare the current character with the corresponding character from the end.
        if converted[i] != converted[len(converted) - i - 1]:
            return False  # If characters don't match, it's not a palindrome.

    # If all characters match, it's a palindrome.
    return True


# Test cases to validate the function.
print("Test Case 1: ", isPalindrome(121))  # Output: True
print("Test Case 2: ", isPalindrome(-121))  # Output: False
print("Test Case 3: ", isPalindrome(10))  # Output: False
print("Test Case 4: ", isPalindrome(12321))  # Output: True
print("Test Case 5: ", isPalindrome(0))  # Output: True
print("Test Case 6: ", isPalindrome(1234321))  # Output: True
