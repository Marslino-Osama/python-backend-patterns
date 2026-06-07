# Two Pointers Learning Guide

## Core Idea

Use two indexes to move through an array or string in a controlled way, usually reducing pair/range checks from O(n²) to O(n).

## The Brute-Force Problem

Check every pair or compare every possible position with nested loops.

## What This Pattern Optimizes

Uses sorted order, symmetry, or a write pointer to avoid repeated comparisons.

## When to Use

Use this pattern when the problem has one or more of these signals:

- sorted array
- in-place
- remove duplicates
- palindrome
- pair
- triplets
- container
- reverse

## Main Types

### Opposite direction

Start at both ends and move inward.

### Same direction fast/slow

Scan with one pointer and write/track with another.

### Sort + two pointers

Sort first, then search pairs/triples predictably.

## Core Invariant

```text
The answer, if it exists, remains inside the active pointer range; or everything before slow is already valid.
```

## Python Template

```python
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
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Moving both pointers when only one should move.
- Using two pointers on unsorted data when sorted order is required.
- Using <= when the same element must not be reused.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Valid Palindrome | Easy | Not Started | |
| Two Sum II - Input Array Is Sorted | Easy | Not Started | |
| Remove Duplicates from Sorted Array | Easy | Not Started | |
| Move Zeroes | Easy | Not Started | |
| Merge Sorted Array | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Container With Most Water | Medium | Not Started | |
| 3Sum | Medium | Not Started | |
| 3Sum Closest | Medium | Not Started | |
| Sort Colors | Medium | Not Started | |
| Partition Labels | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Trapping Rain Water | Hard / Optional | Not Started | |
| 4Sum | Hard / Optional | Not Started | |

## How to Study This Pattern

1. Read the core idea.
2. Write the brute-force approach in plain English.
3. Explain what repeated work the pattern removes.
4. Write the template from memory.
5. Solve the easy problems first.
6. Move to medium problems only after the invariant is clear.
7. Add your accepted solutions inside `solutions/`.
8. Update `notes.md` with mistakes and edge cases.

## Reflection Questions

After every solved problem, answer:

1. Why does this pattern fit?
2. What is the state or pointer meaning?
3. What is the invariant?
4. What edge case failed first?
5. What is the time complexity?
6. What is the space complexity?
7. Could I solve it again without help tomorrow?
