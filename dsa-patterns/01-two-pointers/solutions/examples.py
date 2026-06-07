"""
Small examples for understanding Two Pointers.

These are learning examples, not final LeetCode submissions.
"""


def has_pair_with_sum_sorted(nums, target):
    """
    Example:
    nums = [1, 2, 4, 7, 11], target = 9
    answer = True because 2 + 7 = 9
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return True

        if current < target:
            left += 1
        else:
            right -= 1

    return False


def is_simple_palindrome(text):
    """
    Example:
    text = "racecar" -> True
    text = "hello" -> False
    """
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


def move_zeroes_learning_example(nums):
    """
    Moves all zeroes to the end while keeping non-zero order.

    Example:
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


if __name__ == "__main__":
    print(has_pair_with_sum_sorted([1, 2, 4, 7, 11], 9))
    print(is_simple_palindrome("racecar"))
    print(move_zeroes_learning_example([0, 1, 0, 3, 12]))
