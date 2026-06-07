# 1D DP Learning Guide

## Core Idea

Solve a problem by storing answers to smaller one-dimensional states.

## The Brute-Force Problem

Use recursion that recomputes the same state many times.

## What This Pattern Optimizes

Caches repeated subproblems and builds the answer from previous states.

## When to Use

Use this pattern when the problem has one or more of these signals:

- maximum/minimum
- number of ways
- can reach
- choose or skip
- climb
- rob
- coin change

## Main Types

### Top-down memoization

Recursive solution with cache.

### Bottom-up tabulation

Iterative dp array.

### Space optimization

Keep only previous states when possible.

## Core Invariant

```text
dp[i] stores the solved answer for the prefix/state ending at i.
```

## Python Template

```python
def climb_stairs_style(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # dp[i] = transition from previous states
        pass

    return dp[n]
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Not defining dp state clearly.
- Wrong base cases.
- Updating dp in wrong order.
- Confusing greedy with DP.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Climbing Stairs | Easy | Not Started | |
| Min Cost Climbing Stairs | Easy | Not Started | |
| N-th Tribonacci Number | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| House Robber | Medium | Not Started | |
| Coin Change | Medium | Not Started | |
| Decode Ways | Medium | Not Started | |
| Word Break | Medium | Not Started | |
| Longest Increasing Subsequence | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Word Break II | Hard / Optional | Not Started | |
| Russian Doll Envelopes | Hard / Optional | Not Started | |

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
