# Sliding Window Learning Guide

## Core Idea

Maintain a contiguous window [left, right] and update its state as it expands or shrinks.

## The Brute-Force Problem

Check every possible subarray or substring and recompute its state repeatedly.

## What This Pattern Optimizes

Keeps the current window state so each element enters and leaves at most once.

## When to Use

Use this pattern when the problem has one or more of these signals:

- subarray
- substring
- contiguous
- longest
- shortest
- at most k
- minimum window

## Main Types

### Fixed window

Window size is exactly k.

### Variable window

Window expands then shrinks when invalid.

### Minimum valid window

Shrink while the window satisfies the condition.

## Core Invariant

```text
The state always describes exactly the current window [left, right].
```

## Python Template

```python
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
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Using it for non-contiguous problems.
- Forgetting to remove the left value from state.
- Updating the answer before restoring validity.
- Using if instead of while when repeated shrinking is needed.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Maximum Average Subarray I | Easy | Not Started | |
| Contains Duplicate II | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Longest Substring Without Repeating Characters | Medium | Not Started | |
| Longest Repeating Character Replacement | Medium | Not Started | |
| Max Consecutive Ones III | Medium | Not Started | |
| Minimum Size Subarray Sum | Medium | Not Started | |
| Permutation in String | Medium | Not Started | |
| Find All Anagrams in a String | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Minimum Window Substring | Hard / Optional | Not Started | |
| Sliding Window Maximum | Hard / Optional | Not Started | |

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
