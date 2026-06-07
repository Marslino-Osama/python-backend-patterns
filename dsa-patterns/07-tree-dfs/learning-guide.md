# Tree DFS Learning Guide

## Core Idea

Use recursion to solve a tree by combining answers from children.

## The Brute-Force Problem

For each node, repeatedly recompute subtree information.

## What This Pattern Optimizes

Processes each node once and returns useful information upward.

## When to Use

Use this pattern when the problem has one or more of these signals:

- binary tree
- root
- leaf
- height
- path sum
- lowest common ancestor
- subtree

## Main Types

### Preorder

Process node before children.

### Inorder

Left, node, right for BST ordering.

### Postorder

Process children before node.

### Path recursion

Carry state from root to leaf.

## Core Invariant

```text
The recursive function returns a clearly defined result for the subtree rooted at the current node.
```

## Python Template

```python
def tree_dfs(root):
    if root is None:
        return 0

    left = tree_dfs(root.left)
    right = tree_dfs(root.right)

    return 1 + max(left, right)
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Not defining what recursion returns.
- Using global state without resetting it.
- Confusing path-from-root with path-anywhere.
- Wrong base case for None nodes.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Maximum Depth of Binary Tree | Easy | Not Started | |
| Invert Binary Tree | Easy | Not Started | |
| Same Tree | Easy | Not Started | |
| Path Sum | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Validate Binary Search Tree | Medium | Not Started | |
| Lowest Common Ancestor of a Binary Tree | Medium | Not Started | |
| Binary Tree Right Side View | Medium | Not Started | |
| Diameter of Binary Tree | Medium | Not Started | |
| Path Sum II | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Binary Tree Maximum Path Sum | Hard / Optional | Not Started | |
| Serialize and Deserialize Binary Tree | Hard / Optional | Not Started | |

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
