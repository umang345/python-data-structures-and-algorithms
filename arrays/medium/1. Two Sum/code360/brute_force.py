# https://www.naukri.com/code360/problems/two-sum_839653

def twoSum(arr, target, n):
    
    track = dict()
    result = []

    for index in range(len(arr)):
        numToCheck = target - arr[index]
        if not track.get(numToCheck) is None:
            result.append([arr[index], numToCheck])
            track[numToCheck]-=1
            if track[numToCheck]==0:
                del track[numToCheck]
        else:
            track[arr[index]] = track.get(arr[index],0)+1
    
    if len(result)==0:
        result.append([-1,-1])

    return result


'''
    O(n) + [O(1) -> O(n)]  O(n) O(n^2)

    O(n) 
'''