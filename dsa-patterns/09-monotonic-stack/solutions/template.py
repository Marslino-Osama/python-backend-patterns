"""
Monotonic Stack template.

Write this template from memory before solving problems.
"""

def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            index = stack.pop()
            result[index] = value

        stack.append(i)

    return result
