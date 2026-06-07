# DSA Patterns in Python

This track covers the core algorithmic patterns commonly used in coding interviews and LeetCode-style problem solving.

It is separate from the backend/system-design track. The backend track teaches production engineering. This track teaches data structures, algorithms, implementation discipline, and interview problem-solving.

## Mission

Learn DSA by recognizing patterns, writing clean Python implementations, testing edge cases, and documenting mistakes.

This is not a solution dump. Every pattern should become a small workbook:

- Concept explanation
- Recognition signs
- Core invariant
- Python templates
- LeetCode problem plan
- Personal notes
- Accepted solutions written by you

## Patterns Covered

| # | Pattern | Main Use Case | Status |
|---|---------|---------------|--------|
| 01 | Two Pointers | Sorted arrays, pairs, in-place movement | In Progress |
| 02 | Sliding Window | Contiguous subarrays/substrings | Not Started |
| 03 | Prefix Sum | Fast range queries and subarray sums | Not Started |
| 04 | Binary Search | Search sorted data or monotonic answer spaces | Not Started |
| 05 | DFS | Graph traversal and connected components | Not Started |
| 06 | BFS | Shortest path in unweighted graphs | Not Started |
| 07 | Tree DFS | Tree recursion, path problems, recursion state | Not Started |
| 08 | Heap / Priority Queue | Top K, scheduling, shortest available item | Not Started |
| 09 | Monotonic Stack | Next greater/smaller, ranges, histogram problems | Not Started |
| 10 | Union Find | Connectivity, components, cycle detection | Not Started |
| 11 | Topological Sort | Directed acyclic graph dependency ordering | Not Started |
| 12 | Dijkstra | Shortest path in weighted graphs | Not Started |
| 13 | Backtracking | Combinations, permutations, constraint search | Not Started |
| 14 | 1D DP | Linear recurrence and state transition | Not Started |
| 15 | 2D DP | Grid, string, and two-variable state tables | Not Started |

## Folder Convention

Each pattern folder should contain:

```text
README.md              # Full explanation of the pattern
leetcode-plan.md       # Problems to solve in order
notes.md               # Your mistakes, edge cases, and lessons
solutions/
├── template.py         # Reusable pattern templates
├── examples.py         # Small learning examples
└── solved_problem.py   # Your accepted LeetCode solutions
```

## Study Flow

1. Read the pattern README.
2. Understand the brute-force approach.
3. Understand what repeated work the pattern removes.
4. Write the template from memory.
5. Solve easy problems first.
6. Solve medium problems.
7. Document every mistake in `notes.md`.
8. Re-solve important problems after a few days.

## Completion Rule

A pattern is complete only when you can:

- Recognize it from the problem statement.
- Explain why brute force is inefficient.
- Write the template without looking.
- Handle edge cases.
- Explain time and space complexity.
- Solve at least 5 related problems.
