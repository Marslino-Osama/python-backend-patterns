# Backtracking Learning Guide

## Core Idea

Explore choices recursively, undo choices, and try alternatives.

## The Brute-Force Problem

Generate every possibility without pruning or structure.

## What This Pattern Optimizes

Uses recursion structure, constraints, and pruning to search only valid candidates when possible.

## When to Use

Use this pattern when the problem has one or more of these signals:

- all combinations
- all permutations
- subsets
- generate
- choose
- constraint
- valid board

## Main Types

### Subsets

Choose or skip each item.

### Combinations

Build fixed-size or target-based groups.

### Permutations

Use each item once in different orders.

### Constraint search

Try candidate choices and backtrack when invalid.

## Core Invariant

```text
The current path represents a valid partial solution.
```

## Python Template

```python
def backtrack(path, choices):
    if is_complete(path):
        result.append(path.copy())
        return

    for choice in choices:
        if not is_valid(choice, path):
            continue

        path.append(choice)
        backtrack(path, choices)
        path.pop()
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Forgetting to undo the choice.
- Appending path without copying.
- Not pruning invalid paths early.
- Reusing elements when the problem says use once.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Binary Watch | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Subsets | Medium | Not Started | |
| Combinations | Medium | Not Started | |
| Permutations | Medium | Not Started | |
| Combination Sum | Medium | Not Started | |
| Generate Parentheses | Medium | Not Started | |
| Letter Combinations of a Phone Number | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| N-Queens | Hard / Optional | Not Started | |
| Sudoku Solver | Hard / Optional | Not Started | |
| Word Search II | Hard / Optional | Not Started | |

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
