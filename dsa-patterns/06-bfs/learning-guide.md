# BFS Learning Guide

## Core Idea

Explore nodes level by level using a queue.

## The Brute-Force Problem

Try all paths without respecting distance levels.

## What This Pattern Optimizes

Finds the shortest path in unweighted graphs because it expands by distance.

## When to Use

Use this pattern when the problem has one or more of these signals:

- shortest path
- minimum steps
- level order
- nearest
- unweighted graph
- grid distance

## Main Types

### Single-source BFS

Start from one node.

### Multi-source BFS

Start from many nodes at once.

### Level BFS

Track distance by levels.

## Core Invariant

```text
Nodes popped from the queue are processed in non-decreasing distance order.
```

## Python Template

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    distance = {start: 0}

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Marking visited after popping instead of when pushing.
- Using DFS for shortest unweighted path.
- Forgetting multi-source BFS.
- Not separating levels when level count is needed.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Binary Tree Level Order Traversal | Easy | Not Started | |
| Minimum Depth of Binary Tree | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Rotting Oranges | Medium | Not Started | |
| Walls and Gates | Medium | Not Started | |
| 01 Matrix | Medium | Not Started | |
| Open the Lock | Medium | Not Started | |
| Shortest Path in Binary Matrix | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Word Ladder | Hard / Optional | Not Started | |
| Shortest Path Visiting All Nodes | Hard / Optional | Not Started | |

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
