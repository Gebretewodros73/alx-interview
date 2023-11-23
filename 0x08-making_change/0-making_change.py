#!/usr/bin/python3
"""
Change making module.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    remaining = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining > 0:
        if coin_index >= num_coins:
            return -1

        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
