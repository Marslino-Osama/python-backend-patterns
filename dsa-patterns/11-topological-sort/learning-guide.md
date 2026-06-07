# Topological Sort Learning Guide

## Core Idea

Order nodes in a directed acyclic graph so every prerequisite appears before the dependent node.

## The Brute-Force Problem

Repeatedly scan dependencies or try all possible orderings.

## What This Pattern Optimizes

Processes dependency graph in O(V + E).

## When to Use

Use this pattern when the problem has one or more of these signals:

- course schedule
- prerequisite
- dependency
- build order
- DAG
- directed graph

## Main Types

### Kahn's algorithm

Use indegrees and a queue.

### DFS topological sort

Postorder traversal with cycle detection.

### Cycle detection

If not all nodes are processed, cycle exists.

## Core Invariant

```text
Only nodes with zero remaining prerequisites enter the queue.
```

## Python Template

```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1

    queue = deque([node for node in range(n) if indegree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Reversing edge direction.
- Forgetting cycle detection.
- Using undirected graph logic.
- Not processing isolated nodes.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Add suitable easy problems | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Course Schedule | Medium | Not Started | |
| Course Schedule II | Medium | Not Started | |
| Find Eventual Safe States | Medium | Not Started | |
| Minimum Height Trees | Medium | Not Started | |
| Alien Dictionary | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Parallel Courses III | Hard / Optional | Not Started | |
| Sort Items by Groups Respecting Dependencies | Hard / Optional | Not Started | |

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
