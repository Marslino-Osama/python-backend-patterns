"""
Binary Search template.

Write this template from memory before solving problems.
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def first_true(left, right, condition):
    answer = right + 1

    while left <= right:
        mid = left + (right - left) // 2

        if condition(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
