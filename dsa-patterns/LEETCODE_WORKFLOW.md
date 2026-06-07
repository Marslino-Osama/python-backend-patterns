# LeetCode Workflow

This workflow keeps the DSA track focused on learning, not collecting answers.

## The Loop

For every problem:

1. Read the problem carefully.
2. Identify the likely pattern before writing code.
3. Write the brute-force idea first.
4. Improve it using the pattern.
5. Solve on LeetCode.
6. Test edge cases.
7. After acceptance, copy your final solution into this repo.
8. Update `notes.md`.
9. Update `problem-index.md`.

## Before Solving

Ask:

- What is the input shape?
- Is the input sorted?
- Is the range contiguous?
- Is this a graph/tree?
- Is there a repeated subproblem?
- What is the brute-force solution?
- What repeated work can be removed?

## During Solving

Write the invariant in a comment before implementation.

Example:

```python
# Invariant: everything before slow is valid.
# Invariant: window [left, right] always satisfies the constraint.
# Invariant: heap contains the best k candidates.
```

## After Solving

Add this to the pattern notes:

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
git commit -m "Solve sliding window longest substring"
git push
```
