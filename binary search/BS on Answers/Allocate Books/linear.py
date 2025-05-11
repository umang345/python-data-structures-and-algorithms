from functools import *

def findPages(arr: [int], n: int, m: int) -> int:

    '''
    12 34 67 90    n=4    m=2

    maxPages = 12
    '''
    if m>n:
        return -1

    maxPages = reduce(lambda acc,x : max(acc,x), arr, arr[0])
    totalPages = reduce(lambda acc,x : acc+x, arr,0)

    for maxPageAllowed in range(maxPages, totalPages+1):
        if helper(arr, n, m, maxPageAllowed):
            return maxPageAllowed
    
    return -1

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
    
    
    