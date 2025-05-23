def calculateMinPatforms(at, dt, n):
    
    timeList = []
    for index in range(n):
        timeList.append((at[index], 'A'))
        timeList.append((dt[index], 'D'))
    
    timeList.sort(key=lambda x : (x[0],x[1]))

    maxTrainsNeeded, count = 0,0

    for trainTime in timeList:
        if trainTime[1] == 'A':
            count+=1
            maxTrainsNeeded = max(maxTrainsNeeded, count)
        else:
            count-=1
    
    return maxTrainsNeeded