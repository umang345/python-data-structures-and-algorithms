from math import *
from collections import *
from sys import *
from os import *

def subarraysXor(arr, x):
    
    n = len(arr)
    count = 0

    for index in range(n):
        xor = 0
        for currIndex in range(index,n):
            xor^=arr[currIndex]
            if xor == x:
                count+=1

    return count


'''
TC -> O(n^2)
SC -> O(1)
'''