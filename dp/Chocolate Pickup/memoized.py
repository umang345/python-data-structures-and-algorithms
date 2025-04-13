from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    return helper(0,0,c-1, grid, dict())

def helper(row, alice, bob, grid, cache) -> int:

        rows = len(grid)
        cols = len(grid[0])
        if row >= rows or alice<0 or alice>=cols or bob<0 or bob>=cols:
            return 0

        key = f"{row}-_-{alice}-_-{bob}"
        if not cache.get(key) is None:
            return cache[key]

        currentMoveAmt = grid[row][alice] if alice==bob else (grid[row][alice] + grid[row][bob])
        
        maxAmt = 0
        for aliceMove in range(-1,2):
            for bobMove in range(-1,2):
                currentAmount = helper(row+1, alice+aliceMove, bob+bobMove, grid, cache)
                if currentAmount > maxAmt:
                    maxAmt = currentAmount

        cache[key] =  maxAmt + currentMoveAmt
        return cache[key]