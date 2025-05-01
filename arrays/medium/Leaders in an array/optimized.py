from os import *
from sys import *
from collections import *
from math import *

def findLeaders(elements, n):
    
    leaders = [elements[-1]]
    for index in range(n-2,-1,-1):
        if elements[index] > leaders[-1]:
            leaders.append(elements[index])
    
    return reversed(list(leaders)) 