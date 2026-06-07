# Dijkstra Learning Guide

## Core Idea

Find shortest paths in weighted graphs with non-negative edge weights using a priority queue.

## The Brute-Force Problem

Try all paths or repeatedly scan all unvisited nodes.

## What This Pattern Optimizes

Always expands the currently shortest known candidate path first.

## When to Use

Use this pattern when the problem has one or more of these signals:

- weighted graph
- shortest path
- minimum cost
- network delay
- positive weights
- cheapest route

## Main Types

### Single-source shortest path

Distance from one source to all nodes.

### Grid Dijkstra

Cells are nodes and movement has cost.

### State Dijkstra

Node includes extra state like stops or resources.

## Core Invariant

```text
When a node is finalized with the smallest distance, no shorter path to it remains undiscovered if all weights are non-negative.
```

## Python Template

```python
import heapq
from collections import defaultdict

def dijkstra(edges, source):
    graph = defaultdict(list)

    for src, dst, weight in edges:
        graph[src].append((dst, weight))

    distances = {source: 0}
    heap = [(0, source)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        if current_distance > distances.get(node, float("inf")):
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Using Dijkstra with negative weights.
- Not skipping stale heap entries.
- Confusing BFS with weighted shortest path.
- Forgetting state dimensions in constrained shortest paths.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Add suitable easy problems | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Network Delay Time | Medium | Not Started | |
| Path With Minimum Effort | Medium | Not Started | |
| Cheapest Flights Within K Stops | Medium | Not Started | |
| Minimum Cost to Connect Points | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Swim in Rising Water | Hard / Optional | Not Started | |
| Shortest Path to Get All Keys | Hard / Optional | Not Started | |

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
