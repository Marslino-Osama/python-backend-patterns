# Heap / Priority Queue Learning Guide

## Core Idea

Use a heap when you repeatedly need the smallest, largest, or best-priority item.

## The Brute-Force Problem

Sort repeatedly or scan the whole list every time you need the best item.

## What This Pattern Optimizes

Maintains best item with O(log n) insert/remove instead of repeated O(n) scans or O(n log n) sorts.

## When to Use

Use this pattern when the problem has one or more of these signals:

- top k
- kth largest
- minimum cost
- merge k
- schedule
- closest
- priority

## Main Types

### Min heap

Python default heapq behavior.

### Max heap

Store negative values.

### Fixed-size heap

Keep only k best items.

### Heap for graph algorithms

Dijkstra and best-first search.

## Core Invariant

```text
The heap contains the current best candidates according to the priority rule.
```

## Python Template

```python
import heapq

def top_k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | Usually O(n²) or worse | Depends on problem |
| Pattern-based solution | Usually O(n), O(n log n), or O(V + E) | Depends on state/data structure |

Always write the exact complexity after solving each LeetCode problem.

## Common Mistakes

- Forgetting Python heapq is min-heap only.
- Letting heap grow larger than k.
- Pushing wrong tuple priority order.
- Using heap when a simple sort once is enough.

## LeetCode Plan

### Easy

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Last Stone Weight | Easy | Not Started | |
| Kth Largest Element in a Stream | Easy | Not Started | |

### Medium

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Kth Largest Element in an Array | Medium | Not Started | |
| Top K Frequent Elements | Medium | Not Started | |
| K Closest Points to Origin | Medium | Not Started | |
| Task Scheduler | Medium | Not Started | |
| Merge K Sorted Lists | Medium | Not Started | |

### Hard / Optional

| Problem | Difficulty | Status | Notes |
|---------|------------|--------|-------|
| Find Median from Data Stream | Hard / Optional | Not Started | |
| IPO | Hard / Optional | Not Started | |

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
