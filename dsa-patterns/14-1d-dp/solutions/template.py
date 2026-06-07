"""
1D DP template.

Write this template from memory before solving problems.
"""

def climb_stairs_style(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # dp[i] = transition from previous states
        pass

    return dp[n]
