# Prefix Sum Learning Guide

## Core Idea

Precompute cumulative values so range sums or subarray sums can be answered quickly.

## The Brute-Force Problem

For every range, loop through all elements inside that range to calculate the sum.

## What This Pattern Optimizes

Turns repeated range-sum calculation into subtraction of previous cumulative values.

## When to Use

Use this pattern when the problem has one or more of these signals:

- range sum
- subarray sum
- sum equals k
- number of subarrays
- continuous
- matrix sum

## Main Types

### 1D prefix sum

prefix[i] stores sum before index i.

### Hash map prefix

Store previous prefix frequencies for subarray count problems.

### 2D prefix sum

Answer rectangle sum queries.

## Core Invariant

```text
prefix[i] represents the accumulated value before index i.
```

## Python Template

```python
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
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Off-by-one errors in prefix arrays.
- Forgetting initial prefix 0.
- Using sliding window when negative numbers require prefix sums.
- Confusing prefix value with current element.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Running Sum of 1d Array | Easy | Not Started | |
| Find Pivot Index | Easy | Not Started | |
| Range Sum Query - Immutable | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Subarray Sum Equals K | Medium | Not Started | |
| Product of Array Except Self | Medium | Not Started | |
| Contiguous Array | Medium | Not Started | |
| Subarray Sums Divisible by K | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Maximum Size Subarray Sum Equals k | Hard / Optional | Not Started | |
| Count of Range Sum | Hard / Optional | Not Started | |

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
