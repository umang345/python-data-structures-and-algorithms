def NthRoot(n: int, m: int) -> int:
    if m==0:
        return 0

    root = 1
    currNum = 1
    while currNum < m :
        root+=1
        currNum = power(root, n)

    if currNum == m:
        return root
    
    return -1

def power(n, exp):
    if exp==0:
        return 1
    if exp==1:
        return n 
    
    if exp%2==0:
        return power(n*n, exp/2)
    else:
        return n * power(n,exp-1)

