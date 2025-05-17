from math import *

def minWindow(S, T):
    start = 0
    hashMap = dict()
    targetMap = dict()
    for char in T:
        targetMap[char] = targetMap.get(char,0)+1

    result = ""
    minLength = inf

    for startIndex in range(len(S)):
        hashMap = dict()
        for index in range(startIndex, len(S)):
            hashMap[S[index]] = hashMap.get(S[index],0)+1
            if compareMaps(hashMap, targetMap):
                if checkIfSubsequence(S[startIndex: index+1], T):
                    currLen = index-startIndex+1
                    if currLen < minLength:
                        minLength = currLen
                        result = S[startIndex:index+1]

    
    return result



def compareMaps(map1, target) -> bool:
    for key, val in target.items():
        if val > map1.get(key,0):
            return False
    return True


def checkIfSubsequence(s1, s2) -> bool:
    
    m,n = len(s1), len(s2)
    p1,p2 = 0,0

    while p1<m and p2<n:
        if s1[p1] == s2[p2]:
            p2+=1
        p1+=1

    if p2!=n:
        return False
    
    return True