from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    
    arr.sort()
    maxCount = 1
    currCount = 1

    for index in range(1, n):
        if arr[index]==arr[index-1]:
            continue 
        elif arr[index] == arr[index-1]+1:
            currCount+=1
            if currCount > maxCount:
                maxCount = currCount
        else:
            currCount=1

    if currCount > maxCount:
        maxCount = currCount
    return maxCount


'''
TC    O(nlogn) + O(n)
SC    O(1)
'''
            