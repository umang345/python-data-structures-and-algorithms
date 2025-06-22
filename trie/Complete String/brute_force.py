from sys import *
from collections import *
from math import *

from typing import *

def completeString(n: int, a: List[str])-> str:
    
    stringSet = set()
    for string in a:
        stringSet.add(string)    
    
    result = None

    for string in a:
        flag = True
        for index in range(len(string)):
            strToCheck = string[:index+1] 
            if not strToCheck in stringSet:
                flag = False
                break
        
        if flag:
            if result is None or len(strToCheck)>len(result):
                result = strToCheck
            elif len(strToCheck) == len(result) and strToCheck < result:
                result = strToCheck
                

    if result is None:
        result = "None"
    return result 