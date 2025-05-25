from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    start,end = 0,n-1 

    while start<end:
        if knows(start, end):
            start+=1
        else:
            end-=1
    
    otherCount = 0
    for person in range(n):
        if person == start:
            continue
        if knows(person, start):
            otherCount+=1
        if knows(start, person):
            return -1
    
    if otherCount==n-1:
        return start
    
    return -1