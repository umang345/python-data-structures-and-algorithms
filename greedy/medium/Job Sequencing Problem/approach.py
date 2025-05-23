def jobScheduling(jobs):

    jobList = []
    for job in jobs:
        jobList.append(tuple(job))

    jobList.sort(key=lambda x : x[2], reverse = True)

    schedule = [-1]*(len(jobs)+1)
    count, profit = 0,0

    for job in jobList:
        if updateIfPossible(schedule, job[1]):
            count+=1
            profit+=job[2]
    
    return count, profit

def updateIfPossible(schedule,deadline):
    for index in range(deadline,0,-1):
        if schedule[index]==-1:
            schedule[index] = 1
            return True 
    
    return False