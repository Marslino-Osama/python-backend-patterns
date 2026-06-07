"""
DFS template.

Write this template from memory before solving problems.
"""

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
