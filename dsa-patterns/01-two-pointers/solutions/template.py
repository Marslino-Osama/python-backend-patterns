"""
Two Pointers templates.

These are not complete LeetCode answers.
Use them as mental models while solving.
"""


def opposite_direction_template(nums, target):
    """
    Use when the input is sorted and you need to find a pair.

    Invariant:
    If a valid answer exists, it is inside nums[left:right+1].
    """
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


def palindrome_template(text):
    """
    Use when comparing both ends of a string.

    Invariant:
    Everything outside [left, right] has already matched.
    """
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


def fast_slow_filter_template(nums):
    """
    Use for in-place filtering or removing duplicates.

    Invariant:
    nums[:slow] contains the valid kept elements.
    """
    slow = 0

    for fast in range(len(nums)):
        if should_keep(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1

    return slow


def should_keep(value):
    """
    Replace this with the problem-specific condition.
    """
    return True


def sorted_triplet_template(nums, target):
    """
    Use for problems like 3Sum after sorting.

    Invariant:
    For each fixed i, left/right search the remaining range.
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right]

            if current == target:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current < target:
                left += 1
            else:
                right -= 1

    return result
