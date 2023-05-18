#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    return: the fewest number of coins needed to meet total
        coins value of the coins in your posession
        total the volume or the detemining factor
    """
    if not coins or coins is None:
        return-1
    if total <= 0:
        return 0
    change = 0
    coins =sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= 1
        if (total == 0):
            return change     
    return -1
