# Monotonic Stack Learning Guide

## Core Idea

Maintain a stack in increasing or decreasing order to find next greater/smaller relationships efficiently.

## The Brute-Force Problem

For every index, scan left or right to find the next greater/smaller item.

## What This Pattern Optimizes

Each element is pushed and popped at most once, giving O(n).

## When to Use

Use this pattern when the problem has one or more of these signals:

- next greater
- next smaller
- previous greater
- daily temperatures
- histogram
- span

## Main Types

### Increasing stack

Useful for next smaller or maintaining rising values.

### Decreasing stack

Useful for next greater.

### Index stack

Store indexes to calculate distances or widths.

## Core Invariant

```text
The stack keeps candidates that have not yet found their next greater/smaller answer.
```

## Python Template

```python
def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            index = stack.pop()
            result[index] = value

        stack.append(i)

    return result
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Storing values when indexes are needed.
- Using wrong comparison < vs <=.
- Forgetting remaining stack elements have no answer.
- Not understanding whether stack should be increasing or decreasing.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Next Greater Element I | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Daily Temperatures | Medium | Not Started | |
| Online Stock Span | Medium | Not Started | |
| Next Greater Element II | Medium | Not Started | |
| Remove K Digits | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Largest Rectangle in Histogram | Hard / Optional | Not Started | |
| Maximal Rectangle | Hard / Optional | Not Started | |

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
