# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Time Spent: 20 mins

def lengthOfLastWord(s):
    """
    Finds the length of the last word in a string.

    :type s: str - Input string.
    :rtype: int - Length of the last word.

    Time Complexity: O(n) - Where n is the length of the string.
    Space Complexity: O(n) - Due to the creation of a list from the string.
    """

    # Remove leading and trailing whitespace, and replace multiple spaces with a single space.
    s = " ".join(s.split())

    # Split the string into a list of words using spaces as the delimiter.
    s_list = s.split(" ")

    # Return the length of the last word in the list.
    return len(s_list[-1])


# Test cases to validate the function.
print("Test Case 1: 'Hello World': Length of last word: ",
      lengthOfLastWord("Hello World"))  # Output: 5
print("Test Case 2: '   fly me   to   the moon  ': Length of last word: ",
      lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print("Test Case 3: 'luffy is still joyboy': Length of last word: ",
      lengthOfLastWord("luffy is still joyboy"))  # Output: 6
print("Test Case 4: '   hello   ': Length of last word: ",
      lengthOfLastWord("   hello   "))  # Output: 5
print("Test Case 5: 'a': Length of last word: ",
      lengthOfLastWord("a"))  # Output: 1
print("Test Case 6: '    ': Length of last word: ",
      lengthOfLastWord("    "))  # Output: 0 (edge case: only spaces)
print("Test Case 7: 'the quick brown fox': Length of last word: ",
      lengthOfLastWord("the quick brown fox"))  # Output: 3
print("Test Case 8: 'end of sentence. ': Length of last word: ",
      lengthOfLastWord("end of sentence. "))  # Output: 9
print("Test Case 9: 'multiple    spaces   between   words': Length of last word: ",
      lengthOfLastWord("multiple    spaces   between   words"))  # Output: 5
# Output: 0 (edge case: empty string)
print("Test Case 10: '': Length of last word: ", lengthOfLastWord(""))
