from functools import *
from math import *

def findPages(arr: [int], n: int, m: int) -> int:

    '''
    12 34 67 90    n=4    m=2

    maxPages = 12
    '''
    if m>n:
        return -1

    maxPages = reduce(lambda acc,x : max(acc,x), arr, arr[0])
    totalPages = reduce(lambda acc,x : acc+x, arr,0)

    low,high = maxPages, totalPages
    result = inf
    while low<=high:
        pagesAllowed = low + (high-low)//2
        if helper(arr, n,m,pagesAllowed):
            result = min(result, pagesAllowed)
            high = pagesAllowed-1
        else:
            low = pagesAllowed+1
    
    return result

def helper(arr, booksCount, targetStudents, pagesAllowed):
    students = 1
    currPageCount = 0

    for book in arr:
        currPageCount+=book 
        if currPageCount > pagesAllowed:
            students+=1
            currPageCount = book 
    
    # students+=1
    return students<=targetStudents
    