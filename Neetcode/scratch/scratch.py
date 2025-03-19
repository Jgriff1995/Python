from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """
    Converts a sorted list of integers into a list of range strings.
    For example: [0,1,2,4,5,7] -> ["0->2","4->5","7"]

    Args:
        nums: A sorted list of integers
    Returns:
        List[str]: A list of strings representing ranges
    """
    # Store the ranges as [start, end] pairs
    ranges = []

    # Iterate through each number in the input list
    for num in nums:
        # If ranges exists AND the last range's end value is exactly one less than current number
        # then extend the existing range by updating its end value
        print(f"Current num: {num}")
        if ranges and ranges[-1][1] == num - 1:
            print(
                f"If block has been hit! ranges exists and {ranges[-1][1]} = {num - 1}"
            )

            print(f"updating: Ranges[-1][1]: {ranges[-1][1]} is now {num}")
            ranges[-1][1] = num
            print(f"ranges is now: {ranges}")
        # Otherwise, start a new range with the current number as both start and end
        else:
            print(f"Start of a new range, appending {[num, num]} to ranges")
            ranges.append([num, num])
            print(f"ranges is now: {ranges}")

    # Convert ranges to strings using list comprehension
    # If start (x) equals end (y), return just the number
    # Otherwise return "start->end" format
    return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]


input_example = [0, 1, 2, 4, 5, 7]
print(summaryRanges(input_example))
