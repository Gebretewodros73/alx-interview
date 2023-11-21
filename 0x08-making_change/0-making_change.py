#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number
    of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of
        the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
              If total is 0 or less, return 0.
              If total cannot be met by any number of
              coins you have, return -1.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the
    # minimum number of coins for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins for each total value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, the
    # total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1
