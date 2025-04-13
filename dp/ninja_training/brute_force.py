# https://www.naukri.com/code360/problems/ninja-s-training_3621003


from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    return helper(n, -1, points)

def helper(currentDay:int, lastActivity:int, points:list[list[int]]) -> int :
    if currentDay == 0:
        return 0
    
    maxPoints = 0
    if lastActivity!=0:
        maxPoints = max(maxPoints, points[currentDay-1][0] + helper(currentDay-1, 0, points))

    if lastActivity!=1:
        maxPoints = max(maxPoints, points[currentDay-1][1] + helper(currentDay-1, 1, points))

    if lastActivity!=2:
        maxPoints = max(maxPoints, points[currentDay-1][2] + helper(currentDay-1, 2, points))

    return maxPoints