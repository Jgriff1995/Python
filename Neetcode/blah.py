from typing import List


def totalFruitCorrect(fruits: List[int]) -> int:
    max_fruit_collected = 0
    basket = {}
    left = 0

    # Loop over the length of fruits denoting "right" for the end of window "left" for start
    for right in range(len(fruits)):
        # Add the fruit at fruit[right] to the basket (which is a dictionary and will keep)
        # an index of {fruit: count seen}
        if fruits[right] in basket:
            basket[fruits[right]] += 1
        else:
            basket[fruits[right]] = 1

        # This is the part where we modify our window, Happens in the example when we hit fruits[i] == 3
        # To be able to shift forward, we must first get rid of the "left" elements in basket until the
        # length is satisfied. The dictionary enters the while loop at {1:1, 2:1, 3:1}. Our window is size
        # 2. so we need to remove the "left" element, to make sure our window condition is satisifed.
        # {1:1} /  {2:1, 3:1}. left is incremented by one at the end, to demonstrate that our window:
        # [L    R] has been shifted forward one
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        # Almost labeled this part as easy, but I forgot about right-left + 1
        # I believe this is show the range of our window, where right and left
        # are indices of the boundaries of our window. We add one to this to
        # make sure we are including the entire size of the window. Since
        # only taking right - left will not include the right index itself.
        # Ex. if left is 2 and right is 4, right - left = 2 and we have 3
        # baskets, i.e. holding 3 diff unique fruits
        # which would imply a window of size 2 but the actual window contains
        # 2, 3, and 4. Which is a window size of 3. so adding 1 helps INCLUDE
        # the indexes of the window correctly.
        max_fruit_collected = max(max_fruit_collected, right - left + 1)

    return max_fruit_collected


totalFruitCorrect([1, 2, 3, 2, 2])


"""
SO FAR:

SLIDING WINDOW PROBLEM FOLLOWS A VERY ROUGH SKELETON OF LOGIC:
var = 0 (for max, min, etc. lookups, (max fruits in our previous example))
datastructure (some data structure to represent our window as we loop)
left , right -> start and end of our window of size n (diff each problem)

    Some LOOP (While,for, etc)
        LOGIC HERE PROCESSING DATA THAT IS RELEVANT TO WINDOW
            ANOTHER LOOP/LOGIC:
                THIS LOOP SERVES TO ADJUST OUR WINDOW WHEN NEEDED.
                (i.e. , we found a fruit "3", which means we need to change the window)
                increment Left to account for the datastructure's window changing
        Update our (max,min, length(longest) etc.)
    return var


"""


# 2
def characterReplacement(self, s, k):
    # Initialize a frequency map to track character counts in the current window
    freq = {}
    max_length = 0
    left = 0  # Left pointer of the sliding window

    for right in range(len(s)):
        # Update the frequency of the current character
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Calculate the number of replacements needed in the current window
        # Replacements = window_size - frequency of the most common character
        window_size = right - left + 1
        max_freq = max(freq.values())
        replacements = window_size - max_freq

        # If replacements > k, shrink the window from the left
        if replacements > k:
            freq[s[left]] -= 1  # Decrease the frequency of the left character
            left += 1  # Move the left pointer
        else:
            # Update the maximum window size
            max_length = max(max_length, window_size)

    return max_length


# 3
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1  # Initialize pointers

    while left < right:
        current_sum = numbers[left] + numbers[right]  # Calculate the current sum
        if current_sum == target:
            # Return the indices (1-indexed)
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # Move left pointer to increase the sum
        else:
            right -= 1  # Move right pointer to decrease the sum

    # If no solution is found (though the problem guarantees one)
    return [-1, -1]


# 4
from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key
        anagrams[sorted_s].append(s)

    return list(anagrams.values())


# Example usage:
print(
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
print(group_anagrams([""]))  # Output: [[""]]
print(group_anagrams(["a"]))  # Output: [["a"]]


# 5
# FILL

# 6
import heapq


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Example usage:
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4


# 7
# FILL


# 8
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    max_length = 1
    longest_palindrome = s[0]

    # Transform the string to avoid even/odd length issues
    transformed_s = "#" + "#".join(s) + "#"
    palindrome_lengths = [0] * len(transformed_s)
    center = 0
    right_boundary = 0

    for i in range(len(transformed_s)):
        if i < right_boundary:
            # Mirror index of i with respect to the center
            mirror = 2 * center - i
            palindrome_lengths[i] = min(right_boundary - i, palindrome_lengths[mirror])

        # Expand around the center i
        while (
            i - palindrome_lengths[i] - 1 >= 0
            and i + palindrome_lengths[i] + 1 < len(transformed_s)
            and transformed_s[i - palindrome_lengths[i] - 1] == transformed_s[i + palindrome_lengths[i] + 1]
        ):
            palindrome_lengths[i] += 1

        # Update the center and right boundary if the palindrome expands beyond the current right boundary
        if i + palindrome_lengths[i] > right_boundary:
            center = i
            right_boundary = i + palindrome_lengths[i]

        # Update the longest palindrome found
        if palindrome_lengths[i] > max_length:
            max_length = palindrome_lengths[i]
            longest_palindrome = transformed_s[i - palindrome_lengths[i] : i + palindrome_lengths[i] + 1].replace("#", "")

    return longest_palindrome


def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
            xor ^= num

    return xor
