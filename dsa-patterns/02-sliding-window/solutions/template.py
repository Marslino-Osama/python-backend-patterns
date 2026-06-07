"""
Sliding Window template.

Write this template from memory before solving problems.
"""

def sliding_window_variable(nums):
    left = 0
    best = 0
    state = {}

    for right, value in enumerate(nums):
        # add value to state

        while False:  # replace with invalid condition
            # remove nums[left] from state
            left += 1

        best = max(best, right - left + 1)

    return best
