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

    Minimize the calls to knows
'''

def findCelebrity(n, knows):

    for person in range(n):
        doesThisPersonKnowOther = False 
        for check in range(n):
            if person==check:
                continue
            if knows(person,check):
                doesThisPersonKnowOther = True 
                break
        
        if not doesThisPersonKnowOther:
            knowCount = 0
            for check in range(n):
                if person==check:
                    continue
                if knows(check, person):
                    knowCount+=1
            
            if knowCount==n-1:
                return person 
    
    return -1