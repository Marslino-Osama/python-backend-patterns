# DFS Learning Guide

## Core Idea

Explore a graph deeply before backtracking, using recursion or an explicit stack.

## The Brute-Force Problem

Repeatedly scan all nodes/edges without marking visited nodes.

## What This Pattern Optimizes

Visits every node/edge once and avoids cycles through a visited set.

## When to Use

Use this pattern when the problem has one or more of these signals:

- graph
- connected components
- island
- path exists
- cycle
- recursive traversal

## Main Types

### Recursive DFS

Natural for grids, graphs, and trees.

### Iterative DFS

Use stack to avoid recursion limits.

### DFS with state

Track parent, color, or path state.

## Core Invariant

```text
A visited node is fully handled or currently being explored, so it should not be processed again as new.
```

## Python Template

```python
def dfs_graph(graph, start):
    visited = set()

    def dfs(node):
        if node in visited:
            return

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return visited
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Not marking visited early enough.
- Forgetting grid bounds.
- Revisiting nodes and causing infinite recursion.
- Mutating input when the problem expects preservation.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Flood Fill | Easy | Not Started | |
| Find if Path Exists in Graph | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Number of Islands | Medium | Not Started | |
| Max Area of Island | Medium | Not Started | |
| Clone Graph | Medium | Not Started | |
| Pacific Atlantic Water Flow | Medium | Not Started | |
| Surrounded Regions | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Making A Large Island | Hard / Optional | Not Started | |

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
