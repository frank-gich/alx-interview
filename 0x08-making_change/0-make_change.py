#!/usr/bin/python3

"""
making change function
"""

def makeChange(coins, total):
    
    if not coins in coins is none:
        return -1
   
    if  total <= 0:
        return 0
    change = 0 
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
