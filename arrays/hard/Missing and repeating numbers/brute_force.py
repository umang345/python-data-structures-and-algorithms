from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    
    freq = dict()
    for index in range(1,n+1):
        freq[index] = 0
    for num in arr:
        freq[num]+=1
    

    result = [-1]*2
    for key,val in freq.items():
        if val==0:
            result[0] = key 
        if val==2:
            result[1] = key
    
    return result


'''
TC -> O(n)+O(n)+O(n) -> O(n)
SC -> O(n)
'''