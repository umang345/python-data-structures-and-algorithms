from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    n = len(arr)
    maxLen = 0
    for fixedIndex in range(n):
        currSum = 0
        currLen = 0
        for currIndex in range(fixedIndex, n):
            currLen+=1
            currSum+=arr[currIndex]
            if currSum == 0:
                if maxLen < currLen:
                    maxLen = currLen 
    
    return maxLen

'''
TC -> O(n^2)
SC -> O(1)
'''