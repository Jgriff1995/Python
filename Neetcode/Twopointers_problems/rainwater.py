from typing import List


def trap(height: List[int]) -> int:
    # Handle empty input
    if not height:
        return 0

    total_water = 0
    # Initialize two pointers at the start and end of array
    left, right = 0, len(height) - 1
    # Keep track of maximum height seen from left and right
    left_max, right_max = 0, 0

    while left < right:
        # Compare heights at left and right pointers
        # Work with the smaller height first
        if height[left] < height[right]:
            # Update left_max if current height is greater
            if height[left] >= left_max:
                left_max = height[left]
            else:
                # Add trapped water based on the difference between left_max and current height
                total_water += left_max - height[left]
            # Move left pointer inward
            left += 1
        else:
            # Update right_max if current height is greater
            if height[right] >= right_max:
                right_max = height[right]
            else:
                # Add trapped water based on the difference between right_max and current height
                total_water += right_max - height[right]
            # Move right pointer inward
            right -= 1

    return total_water


print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))

