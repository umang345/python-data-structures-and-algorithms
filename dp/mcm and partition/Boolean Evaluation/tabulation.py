def evaluateExp(exp: str) -> int:
    cache = [[[0 for target in range(2)] for end in range(len(exp))] for start in range(len(exp))]

    n = len(exp)
    mod = (10**9)+7
    for start in range(n-1,-1,-1):
        for end in range(start, n):
            for target in range(2):
                if start == end:
                    if target == 1:
                        if exp[start] == 'T':
                            cache[start][end][target]=1
                    else:
                        if exp[start] == 'F':
                            cache[start][end][target]=1
                    continue
                count = 0
                for op in range(start+1, end, 2):
                    leftTrue = cache[start][op-1][1]%mod
                    leftFalse = cache[start][op-1][0]%mod
                    rightTrue = cache[op+1][end][1]%mod
                    rightFalse = cache[op+1][end][0]%mod

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


    return cache[0][n-1][1]