from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    return helper(n-1, k, arr)

def helper(index:int, target:int, arr:list[int])->bool:
    if target==0:
        return True 
    
    if index<0:
        return False

    if arr[index] > target:
        return helper(index-1,target, arr)
    else:
        return helper(index-1, target-arr[index], arr) or helper(index-1, target, arr)
    
    
    

