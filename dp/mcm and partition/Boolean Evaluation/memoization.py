def evaluateExp(exp: str) -> int:
    cache = [[[-1 for target in range(2)] for end in range(len(exp))] for start in range(len(exp))]
    return helper(0, len(exp)-1, 1, exp, cache)
    
def helper(start, end, target, exp,cache) -> int:
    if start==end:
        if target == 1:
            if exp[start] == 'T':
                return 1
            else:
                return 0
            # return 1 if exp[start] == 'T' else 0
        else:
            if exp[start] == 'F':
                return 1
            else:
                return 0

    if cache[start][end][target] != -1:
        return cache[start][end][target]

    mod = (10**9)+7
    count = 0


    for op in range(start+1, end, 2):
        leftTrue = helper(start, op-1, 1, exp,cache)%mod
        leftFalse = helper(start, op-1, 0, exp,cache)%mod
        rightTrue = helper(op+1,end, 1, exp,cache)%mod
        rightFalse = helper(op+1, end, 0, exp,cache)%mod

        if exp[op] == '|':
            if target == 1:
                count = count + ((leftTrue*rightTrue)+(leftTrue*rightFalse)+(leftFalse*rightTrue)) 
            else:
                count = count + (leftFalse*rightFalse)
        elif exp[op] == '&':
            if target == 1:
                count = count + (leftTrue*rightTrue)
            else:
                count = count + ((leftFalse*rightTrue)+(leftTrue*rightFalse)+(leftFalse*rightFalse))
        else:
            if target == 1:
                count = count + ((leftTrue*rightFalse)+(leftFalse*rightTrue))
            else:
                count = count + ((leftTrue*rightTrue)+(leftFalse*rightFalse))

        count = count%mod 

    cache[start][end][target] = count 
    return cache[start][end][target]