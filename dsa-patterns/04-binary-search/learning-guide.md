# Binary Search Learning Guide

## Core Idea

Repeatedly cut a sorted or monotonic search space in half.

## The Brute-Force Problem

Scan every possible value or index linearly.

## What This Pattern Optimizes

Uses monotonic behavior to discard half of the search space each step.

## When to Use

Use this pattern when the problem has one or more of these signals:

- sorted
- minimum possible
- maximum possible
- search
- first occurrence
- last occurrence
- answer space

## Main Types

### Classic index search

Find a target in sorted data.

### Boundary search

Find first true or last false.

### Binary search on answer

Search a numeric answer space using a feasibility check.

## Core Invariant

```text
The target/boundary answer remains inside the current search range.
```

## Python Template

```python
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
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Wrong loop condition.
- Infinite loop from not moving boundaries.
- Returning mid instead of stored answer in boundary search.
- Not proving monotonicity before binary searching.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Binary Search | Easy | Not Started | |
| Search Insert Position | Easy | Not Started | |
| First Bad Version | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Find First and Last Position of Element | Medium | Not Started | |
| Search in Rotated Sorted Array | Medium | Not Started | |
| Find Minimum in Rotated Sorted Array | Medium | Not Started | |
| Koko Eating Bananas | Medium | Not Started | |
| Capacity To Ship Packages Within D Days | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Median of Two Sorted Arrays | Hard / Optional | Not Started | |
| Split Array Largest Sum | Hard / Optional | Not Started | |

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
