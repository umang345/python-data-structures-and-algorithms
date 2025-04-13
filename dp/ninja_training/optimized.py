from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    return helper(n, -1, points, dict())

def helper(currentDay:int, lastActivity:int, points:list[list[int]], mem:dict) -> int :
    if currentDay == 0:
        return 0

    key = f"{currentDay}-_-{lastActivity}"
    if not mem.get(key) is None:
        return mem[key]

    maxPoints = 0
    if lastActivity!=0:
        maxPoints = max(maxPoints, points[currentDay-1][0] + helper(currentDay-1, 0, points, mem))

    if lastActivity!=1:
        maxPoints = max(maxPoints, points[currentDay-1][1] + helper(currentDay-1, 1, points, mem))

    if lastActivity!=2:
        maxPoints = max(maxPoints, points[currentDay-1][2] + helper(currentDay-1, 2, points, mem))

    mem[key] = maxPoints
    return maxPoints