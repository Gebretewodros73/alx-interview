#!/usr/bin/python3
"""Change making module."""
import sys


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Initialize a table to store minimum coins needed for each amount
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0

    # Update the table using each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != sys.maxsize else -1
