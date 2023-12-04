#!/usr/bin/python3
"""
Prime Game module.
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        maria_turn = True

        while primes:
            chosen_prime = max(primes) if maria_turn else min(primes)
            primes = [p for p in primes if p % chosen_prime != 0]
            maria_turn = not maria_turn

        if maria_turn:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
