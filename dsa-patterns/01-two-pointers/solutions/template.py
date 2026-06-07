"""
Two Pointers template.

Write this template from memory before solving problems.
"""

def two_pointers_sorted_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1

    return None
