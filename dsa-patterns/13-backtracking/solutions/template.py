"""
Backtracking template.

Write this template from memory before solving problems.
"""

def backtrack(path, choices):
    if is_complete(path):
        result.append(path.copy())
        return

    for choice in choices:
        if not is_valid(choice, path):
            continue

        path.append(choice)
        backtrack(path, choices)
        path.pop()
