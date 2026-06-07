"""
2D DP template.

Write this template from memory before solving problems.
"""

def grid_dp(rows, cols):
    dp = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            # dp[r][c] = transition from previous states
            pass

    return dp[rows - 1][cols - 1]
