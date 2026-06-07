"""
Topological Sort template.

Write this template from memory before solving problems.
"""

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
