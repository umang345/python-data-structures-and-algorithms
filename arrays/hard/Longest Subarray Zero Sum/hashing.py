from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    maxLen = 0
    hashMap = dict()
    currSum = 0
    hashMap[0] = -1

    for index,num in enumerate(arr):
        currSum+=num 
        target = currSum
        if not hashMap.get(target) is None:
            currLen = index - hashMap[target]
            if maxLen < currLen:
                maxLen = currLen

        if hashMap.get(currSum) is None:
            hashMap[currSum] = index

    return maxLen 