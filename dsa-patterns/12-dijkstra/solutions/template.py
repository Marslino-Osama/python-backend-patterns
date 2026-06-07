"""
Dijkstra template.

Write this template from memory before solving problems.
"""

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
