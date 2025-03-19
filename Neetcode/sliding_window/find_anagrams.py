from typing import List
from collections import defaultdict


def findAnagrams(s: str, p: str) -> List[int]:
    hashMap = defaultdict(int)
    result = []
    length_p = len(p)
    length_s = len(s)

    if length_p > length_s:
        return []

    for character in p:
        hashMap[character] += 1

    for i in range(length_p - 1):
        if s[i] in hashMap:
            hashMap[s[i]] -= 1

    for i in range(-1, length_s - length_p + 1):
        if i > -1 and s[i] in hashMap:
            hashMap[s[i]] += 1
        if i + length_p < length_s and s[i + length_p] in hashMap:
            hashMap[s[i + length_p]] -= 1

        if all(v == 0 for v in hashMap.values()):
            result.append(i + 1)

    return result


print(findAnagrams("cbaebabacd", "abc"))


def findAnagramsV1(s: str, p: str) -> List[int]:

    result = []
    n = len(p)
    start, end = 0, len(s)

    p_count = defaultdict(int)
    for char in p:
        p_count[char] += 1

    window_count = defaultdict(int)
    for char in s[start : start + n]:
        window_count[char] += 1

    while start + n <= end:
        if window_count == p_count:
            result.append(start)
        window_count[s[start]] -= 1
        if window_count[s[start]] == 0:
            del window_count[s[start]]
        if start + n < end:
            window_count[s[start + n]] += 1
        start += 1

    return result


print(findAnagramsV1("cbaebabacd", "abc"))


def findAnagramsV0(s: str, p: str) -> List[int]:
    result = []
    n = len(p)
    start, end = 0, len(s)
    p = sorted(p)
    current_substring = s[start : start + n]
    while start < end:
        if sorted(current_substring) == p:
            result.append(start)
            start += 1
            current_substring = s[start : start + n]
        else:
            start += 1
            current_substring = s[start : start + n]

    return result


print(findAnagramsV0("cbaebabacd", "abc"))
