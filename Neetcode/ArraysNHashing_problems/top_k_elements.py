from typing import List

"""
* Given an integer array nums and an integer k, return the k most frequent elements.

! Input: list[nums], int k

! output: list[int]
"""


def topKFrequent(nums: List[int], k: int) -> List[int]:
    result = {}

    # Populate the dictionary with the frequency of each element in nums
    for num in nums:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1

    # Sort the dictionary by frequency and return the top k elements
    return list({k: v for k, v in sorted(result.items(), key=lambda item: item[1])})[
        -k:
    ]


def topKFrequentBucketSort(nums: List[int], k: int) -> List[int]:
    count = {}
    # Create a list of empty lists to use as buckets for frequencies add + 1 to len
    # to make the indexes of the list correspond to the number freq
    freq = [[] for i in range(len(nums) + 1)]

    # Count the frequency of each element in nums
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    # Place elements into the corresponding frequency bucket
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []

    print(freq)
    # Iterate over the buckets in reverse order to get the most frequent elements
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            print(num)
            res.append(num)
            if len(res) == k:
                return res


topKFrequentBucketSort([1], 1)
