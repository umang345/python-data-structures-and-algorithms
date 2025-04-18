def lcs(str1: str, str2: str) -> int:
    
    n = len(str1)
    m = len(str2)
    mem = [0 for colIndex in range(m+1)]

    currentMax = 0

    for rowIndex in range(1, n+1):
        tempCache = [0 for colIndex in range(m+1)]
        for colIndex in range(1, m+1):
            if str1[rowIndex-1] == str2[colIndex-1]:
                tempCache[colIndex] = mem[colIndex-1]+1
                if currentMax < tempCache[colIndex]:
                    currentMax = tempCache[colIndex]

        for cacheIndex in range(m+1):
            mem[cacheIndex] = tempCache[cacheIndex]

    return currentMax