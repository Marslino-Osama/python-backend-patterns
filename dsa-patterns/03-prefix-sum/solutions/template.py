"""
Prefix Sum template.

Write this template from memory before solving problems.
"""

def prefix_sum(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    # sum from left to right inclusive:
    # prefix[right + 1] - prefix[left]
    return prefix


def count_subarrays_sum_k(nums, k):
    count = 0
    current = 0
    seen = {0: 1}

    for num in nums:
        current += num
        count += seen.get(current - k, 0)
        seen[current] = seen.get(current, 0) + 1

    return count
