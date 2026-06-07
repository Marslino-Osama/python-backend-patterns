# Union Find Learning Guide

## Core Idea

Track connected components with efficient union and find operations.

## The Brute-Force Problem

Run DFS/BFS repeatedly to check whether nodes are connected.

## What This Pattern Optimizes

Answers connectivity changes almost in O(1) amortized time using path compression and union by rank/size.

## When to Use

Use this pattern when the problem has one or more of these signals:

- connected components
- groups
- friend circles
- redundant connection
- cycle in undirected graph
- merge accounts

## Main Types

### Basic DSU

Parent array only.

### Path compression

Flatten tree during find.

### Union by size/rank

Attach smaller tree under larger tree.

## Core Invariant

```text
Every node points, directly or indirectly, to a representative root of its component.
```

## Python Template

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Forgetting path compression.
- Not using union by size/rank.
- Confusing node labels with zero-based indexes.
- Using Union Find for directed dependency problems where topological sort is needed.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Find if Path Exists in Graph | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Number of Connected Components in an Undirected Graph | Medium | Not Started | |
| Redundant Connection | Medium | Not Started | |
| Accounts Merge | Medium | Not Started | |
| Number of Provinces | Medium | Not Started | |
| Graph Valid Tree | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Making A Large Island | Hard / Optional | Not Started | |
| Bricks Falling When Hit | Hard / Optional | Not Started | |

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
