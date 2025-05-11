from math import *

def upperBound(row,k):
    low, high = 0, len(row)-1

    while low<=high:
        mid = low+(high-low)//2
        
        if row[mid]<=k:
            low = mid+1
        else:
            high = mid-1

    return low

def getElementsLessThanK(matrix, k):
    count = 0
    for row in matrix:
        count+=upperBound(row,k)
    
    return count
    

def getMedian(matrix):
    
    minElement, maxElement = inf, -inf
    rows, cols = len(matrix), len(matrix[0])

    for index in range(rows):
        minElement = min(minElement, matrix[index][0])
        maxElement = max(maxElement, matrix[index][cols-1])

    low, high = minElement, maxElement

    required = ceil((rows*cols)/2)
    result = -inf

    while low<=high:
        mid = low + (high-low)//2

        elementsLessThanMid = getElementsLessThanK(matrix, mid)
        if elementsLessThanMid>=required:
            result = mid
            high = mid-1
        else:
            low = mid+1
    
    return result