# LeetCode Workflow

This file defines how to use the DSA track while solving problems on LeetCode.

The goal is not to collect answers. The goal is to build pattern recognition, implementation speed, and the ability to explain your solution clearly.

## The Loop

For every problem:

1. Read the problem carefully.
2. Identify the pattern before writing code.
3. Write the brute-force idea first.
4. Improve it using the pattern.
5. Write the solution on LeetCode.
6. Test edge cases.
7. After solving, copy your final accepted solution into this repo.
8. Update `notes.md` with mistakes, edge cases, and lessons learned.
9. Update `problem-index.md`.

## Before Solving

Ask yourself:

- What is the input shape?
- Is the input sorted?
- Do I need a contiguous range?
- Do I need to search a graph/tree?
- Is there a repeated subproblem?
- What would the brute-force solution be?
- Why is brute force too slow?
- What pattern removes the wasted work?

## During Solving

Write the invariant in a comment before implementation.

Examples:

```python
# Invariant: everything before `slow` is valid and kept.
# Invariant: window [left, right] always satisfies the current constraint.
# Invariant: heap contains the best candidates seen so far.
```

This forces you to understand the algorithm instead of only writing code.

## After Solving

Add a short reflection:

```text
Problem:
Pattern:
Why this pattern:
Time complexity:
Space complexity:
Mistake:
Edge case:
Would I solve it again without help? yes/no
```

## Commit Style

Use small commits:

```bash
git add .
git commit -m "Solve two pointers valid palindrome"
git push
```

## What Not To Do

- Do not paste full solutions before trying.
- Do not memorize code line by line.
- Do not skip edge cases.
- Do not move to harder problems until the template feels natural.
- Do not count a problem as solved if you cannot explain why the pattern works.
