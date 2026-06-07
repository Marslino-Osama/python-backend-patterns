"""
BFS template.

Write this template from memory before solving problems.
"""

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
