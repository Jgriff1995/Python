# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy
# Time Spent: 30 mins

def strStr(haystack, needle):
    """
    Finds the index of the first occurrence of `needle` in `haystack`.

    :type haystack: str - The string to search within.
    :type needle: str - The string to search for.
    :rtype: int - The index of the first occurrence of `needle` in `haystack`, or -1 if not found.

    Time Complexity: O(n * m) - Where n is the length of `haystack` and m is the length of `needle`.
    Space Complexity: O(1) - Constant space, as no additional data structures are used.
    """

    # Iterate over the length of `haystack`.
    for i in range(len(haystack)):
        # If we find a match for the first character of `needle`.
        if needle[0] == haystack[i]:
            # Take a substring from the index `i` to the length of `needle`.
            temp = haystack[i:i + len(needle)]
            # Check if this substring matches `needle`.
            if temp == needle:
                # Return the index `i` since the substring matches `needle`.
                return i

    # If `needle` is not found in `haystack`, return -1.
    return -1


# Test cases to validate the function.
print("Test Case 1: ", strStr("sadbutsad", "sad"))  # Output: 0
print("Test Case 2: ", strStr("sabdcdasb", "da"))  # Output: -1
print("Test Case 3: ", strStr("leetcode", "leeto"))  # Output: -1
print("Test Case 4: ", strStr("hello", "ll"))  # Output: 2
print("Test Case 5: ", strStr("aaaaa", "bba"))  # Output: -1
print("Test Case 6: ", strStr("mississippi", "issip"))  # Output: 4
# Output: 0 (edge case: single character match)
print("Test Case 9: ", strStr("a", "a"))
print("Test Case 10: ", strStr("abcde", "fgh"))  # Output: -1 (no match)
