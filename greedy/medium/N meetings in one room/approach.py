from typing import List

'''
sort according to end time
'''

def maximumMeetings(start: List[int], end: List[int]) -> int:
    timePairs = []
    for index in range(len(start)):
        timePairs.append((start[index], end[index]))
    
    timePairs.sort(key=lambda x : x[1])

    endTime = 0
    count=0

    for timePair in timePairs:
        if endTime < timePair[0]:
            count+=1
            endTime = timePair[1]
        
    return count 