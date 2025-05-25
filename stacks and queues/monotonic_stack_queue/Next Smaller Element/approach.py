from collections import deque

def nextSmallerElement(arr,n):
    
    result = [-1]*n
    stack = deque()

    for index in range(n-1,-1,-1):
        while len(stack)>0 and stack[0] >= arr[index]:
            stack.popleft()
        
        if len(stack)>0:
            result[index] = stack[0]
        
        stack.appendleft(arr[index])
    
    return result