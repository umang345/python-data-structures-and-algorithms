from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    if n == 0:
        return 0

    task1, task2,task3=0,0,0

    for index in range(1, n+1):
        
        updated1 = points[index-1][0]+max(task2, task3)
        updated2 = points[index-1][1]+max(task1, task3)
        updated3 = points[index-1][2]+max(task1, task2)
        task1 = updated1
        task2 = updated2
        task3 = updated3

    return max(
        task1,
        max(
            task2, task3
        )
    )



