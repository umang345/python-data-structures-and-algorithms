from typing import List
import heapq

def sjf(n: int, arrivalTime: List[int], burstTime: List[int]) -> float:
    
    
    process = []
    for index in range(n):
        process.append((arrivalTime[index], burstTime[index]))
    
    process.sort(key=lambda x : (x[0],x[1]))
    pq = []

    heapq.heappush(pq, (process[0][1] ,process[0]))

    currTime = process[0][0]
    waitTime = 0
    processIndex = 1

    while len(pq)>0:
         
        _,currProcess = heapq.heappop(pq)
        waitTime+=(currTime-currProcess[0])
        currTime+=currProcess[1]

        while processIndex<n and process[processIndex][0] <= currTime:
            heapq.heappush(pq, (process[processIndex][1] ,process[processIndex]))
            processIndex+=1
        
        if len(pq)==0 and processIndex<n:
            heapq.heappush(pq, (process[processIndex][1] ,process[processIndex]))
            currTime+=(process[processIndex][1] - currTime)
            processIndex+=1
    
    return waitTime/n