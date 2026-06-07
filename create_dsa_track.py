from pathlib import Path

root = Path("dsa-patterns")

patterns = [
    ("01-two-pointers", "Two Pointers", "Use two indexes moving through an array/string to reduce nested loops."),
    ("02-sliding-window", "Sliding Window", "Use a moving window for contiguous subarray or substring problems."),
    ("03-prefix-sum", "Prefix Sum", "Precompute cumulative sums to answer range/subarray queries fast."),
    ("04-binary-search", "Binary Search", "Search sorted data or a monotonic answer space."),
    ("05-dfs", "DFS", "Explore graph paths deeply using recursion or a stack."),
    ("06-bfs", "BFS", "Explore graph levels using a queue, usually for shortest path in unweighted graphs."),
    ("07-tree-dfs", "Tree DFS", "Use recursion on trees for path, depth, subtree, and traversal problems."),
    ("08-heap-priority-queue", "Heap / Priority Queue", "Use a heap when you repeatedly need min/max/top-k elements."),
    ("09-monotonic-stack", "Monotonic Stack", "Maintain increasing/decreasing stack for next greater/smaller and range problems."),
    ("10-union-find", "Union Find", "Track connected components efficiently using parent and rank/size arrays."),
    ("11-topological-sort", "Topological Sort", "Order directed acyclic graph nodes based on dependencies."),
    ("12-dijkstra", "Dijkstra", "Find shortest paths in weighted graphs with non-negative edge weights."),
    ("13-backtracking", "Backtracking", "Explore choices recursively and undo choices when returning."),
    ("14-1d-dp", "1D DP", "Solve problems using one-dimensional state transitions."),
    ("15-2d-dp", "2D DP", "Solve grid, string, or two-variable state problems using a table."),
]

root.mkdir(exist_ok=True)

(root / "README.md").write_text("""# DSA Patterns in Python

This track covers the core algorithmic patterns commonly used in coding interviews and problem solving.

It is separate from the backend/system-design track. The backend track teaches production engineering. This track teaches data structures, algorithms, and interview-style problem solving.

## Patterns Covered

| # | Pattern | Status |
|---|---------|--------|
| 01 | Two Pointers | Not Started |
| 02 | Sliding Window | Not Started |
| 03 | Prefix Sum | Not Started |
| 04 | Binary Search | Not Started |
| 05 | DFS | Not Started |
| 06 | BFS | Not Started |
| 07 | Tree DFS | Not Started |
| 08 | Heap / Priority Queue | Not Started |
| 09 | Monotonic Stack | Not Started |
| 10 | Union Find | Not Started |
| 11 | Topological Sort | Not Started |
| 12 | Dijkstra | Not Started |
| 13 | Backtracking | Not Started |
| 14 | 1D DP | Not Started |
| 15 | 2D DP | Not Started |

## Study Flow

1. Read the pattern README.
2. Understand when to use the pattern.
3. Write the template from memory.
4. Solve easy problems first.
5. Move to medium problems.
6. Document mistakes in `notes.md`.
7. Re-solve problems after a few days without looking.

## Rule

Do not memorize full solutions. Learn the pattern, invariant, state, edge cases, and complexity.
""", encoding="utf-8")

(root / "PATTERN_TEMPLATE.md").write_text("""# Pattern Template

## Pattern Name

## When to Use

## Recognition Signs

## Core Idea

## Python Template

```python
def solve():
    pass