# 2D DP Learning Guide

## Core Idea

Use a table where each state depends on two variables, often index pairs, grid cells, or two strings.

## The Brute-Force Problem

Try all recursive possibilities and recompute overlapping states.

## What This Pattern Optimizes

Stores results for every pair/state so each subproblem is solved once.

## When to Use

Use this pattern when the problem has one or more of these signals:

- two strings
- grid
- matrix
- edit distance
- longest common
- subsequence
- interval

## Main Types

### Grid DP

dp[row][col] from top/left neighbors.

### String DP

dp[i][j] for prefixes of two strings.

### Interval DP

dp[left][right] for ranges.

## Core Invariant

```text
dp[i][j] stores the answer for a clearly defined two-dimensional subproblem.
```

## Python Template

```python
def grid_dp(rows, cols):
    dp = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            # dp[r][c] = transition from previous states
            pass

    return dp[rows - 1][cols - 1]
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Not defining what i and j mean.
- Wrong table dimensions.
- Wrong iteration order.
- Forgetting empty-prefix base row/column.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Add suitable easy problems | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Unique Paths | Medium | Not Started | |
| Minimum Path Sum | Medium | Not Started | |
| Longest Common Subsequence | Medium | Not Started | |
| Edit Distance | Medium | Not Started | |
| Coin Change II | Medium | Not Started | |
| Longest Palindromic Substring | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Regular Expression Matching | Hard / Optional | Not Started | |
| Burst Balloons | Hard / Optional | Not Started | |
| Palindrome Partitioning II | Hard / Optional | Not Started | |

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
