"""
Tree DFS template.

Write this template from memory before solving problems.
"""

def tree_dfs(root):
    if root is None:
        return 0

    left = tree_dfs(root.left)
    right = tree_dfs(root.right)

    return 1 + max(left, right)
