from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    '''
    totalsum = 1+2+x+4+5
    currSum = 1+2+y+4+5

    totalsum - currSum = x-y

    totalSum2 = 1^2 + 2^2 + .... + 5^2
    currSum2 = 1^2 + 2^2 + ..... + 5^2

    totalSum2 - currSum2 = x^2 - y^2 = (x+y)(x-y)

    x+y = (totalSum2 - currSum2)/(x-y)

    x-y = xMinusy
    x+y = xPlusy

    x = (xMinusy+xPlusy)/2

    y = (xPlusy-xMinusy)/2

    [5,4,2,4,1]     m=3, r=4
    totalSum = 15           totalSum - currSum = -1
    currSum = 16

    totalSum2 = 225
    currSum2 = 256           totalSum2 - currSum2 = -31

    x-y = -1
    x+y = 31

    x = 30/2 = 15
    '''
    
    totalSum, currSum = 0,0
    totalSum2 = 0
    currSum2 = 0

    for index in range(n):
        totalSum+=(index+1)
        currSum+=(arr[index])
        totalSum2+=((index+1)*(index+1))
        currSum2+=((arr[index])*(arr[index]))

    xMinusy = totalSum-currSum
    xPlusy = (totalSum2 - currSum2)//(xMinusy)

    x = (xMinusy+xPlusy)//2
    y = (xPlusy-xMinusy)//2

    for num in arr:
        if num == x:
            return [y,x]
    
    return [x,y]


'''
TC -> O(n) + O(n)
SC -> O(1)
'''