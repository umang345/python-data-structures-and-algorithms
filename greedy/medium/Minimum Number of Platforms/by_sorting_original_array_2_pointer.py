def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    p1,p2 = 0,0

    count, maxCount = 0, 0
    while p1<n and p2<n:
        if at[p1]<=dt[p2]:
            count+=1
            maxCount = max(maxCount, count)
            p1+=1
        else:
            p2+=1
            count-=1
    
    return maxCount