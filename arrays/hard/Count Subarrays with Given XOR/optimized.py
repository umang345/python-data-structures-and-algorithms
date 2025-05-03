from math import *
from collections import *
from sys import *
from os import *

def subarraysXor(arr, x):

    hashMap = dict()
    n = len(arr)
    count = 0
    xor = 0
    hashMap[0] = 1

    for num in arr:
        xor^=num 
        target = xor^x 
        if not hashMap.get(target) is None:
            count+=hashMap[target]

        hashMap[xor] = hashMap.get(xor,0)+1

    return count

'''
TC  -> O(n)
SC  -> O(n)
'''