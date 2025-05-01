from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    
    hashSet = set([num for num in arr])
    maxLen = 0

    for element in hashSet:
        if element-1 in hashSet:
            continue 
        else:
            numToCheck = element
            count = 0
            while numToCheck in hashSet:
                count+=1
                numToCheck+=1
            
            if count > maxLen:
                maxLen = count 
    
    return maxLen 


'''
TC     O(N)+ O(N)
SC     O(N)
'''
