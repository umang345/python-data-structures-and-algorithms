def lcs(str1: str, str2: str) -> int:
    
    n = len(str1)
    m = len(str2)
    mem = [[0 for colIndex in range(m+1)] for rowIndex in range(n+1)]

    currentMax = 0

    for rowIndex in range(1, n+1):
        for colIndex in range(1, m+1):
            if str1[rowIndex-1] == str2[colIndex-1]:
                mem[rowIndex][colIndex] = mem[rowIndex-1][colIndex-1]+1
                if currentMax < mem[rowIndex][colIndex]:
                    currentMax = mem[rowIndex][colIndex]

    return currentMax
