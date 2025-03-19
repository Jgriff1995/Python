# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Time Spent: 1hr

def longestCommonPrefix(strs):
    """
    Finds the longest common prefix among an array of strings.

    :type strs: List[str] - Input list of strings.
    :rtype: str - The longest common prefix. Returns an empty string if no common prefix exists.

    Time Complexity: O(n * m) - Where n is the number of strings and m is the length of the shortest string.
    Space Complexity: O(1) - Constant space, as we only store the result string.
    """

    # Variable to store the longest common prefix.
    longest_prefix = ""

    # Edge case: If the input list is empty, return an empty string.
    if not strs:
        return longest_prefix

    # Iterate through the characters of the shortest string in the list.
    for i in range(len(min(strs))):
        # Compare the current character of the first string with the corresponding character in all other strings.
        for j in range(1, len(strs)):
            if strs[0][i] != strs[j][i]:
                # If characters don't match, return the current longest prefix.
                return longest_prefix

        # If all characters match, add the current character to the longest prefix.
        longest_prefix += strs[0][i]

    # Return the longest common prefix found.
    return longest_prefix


# Test cases to validate the function.
print("Test Case 1: ", longestCommonPrefix(
    ["flower", "flow", "flight"]))  # Output: "fl"
print("Test Case 2: ", longestCommonPrefix(
    ["dog", "racecar", "car"]))  # Output: ""
print("Test Case 3: ", longestCommonPrefix(
    ["apple", "apple", "apple"]))  # Output: "apple"
print("Test Case 4: ", longestCommonPrefix(["hello"]))  # Output: "hello"
print("Test Case 5: ", longestCommonPrefix([]))  # Output: ""
print("Test Case 6: ", longestCommonPrefix(
    ["interspecies", "interstellar", "interstate"]))  # Output: "inters"
