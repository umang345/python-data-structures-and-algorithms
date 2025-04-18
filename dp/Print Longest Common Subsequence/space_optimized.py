def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    cache = ["" for colIndex in range(m+1)]
    
    for rowIndex in range(1, n+1):
        tempCache = ["" for colIndex in range(m+1)]
        for colIndex in range(1, m+1):

            if s1[rowIndex-1] == s2[colIndex-1]:
                tempCache[colIndex] = cache[colIndex-1] + s1[rowIndex-1]
            else:
                neitherIncluded = cache[colIndex-1]
                text1Included = cache[colIndex]
                text2Included = tempCache[colIndex-1]

                if len(neitherIncluded) >= len(text1Included) and len(neitherIncluded) >= len(text2Included):
                    tempCache[colIndex] = neitherIncluded
                elif len(text1Included) >= len(neitherIncluded) and len(text1Included) >= len(text2Included):
                    tempCache[colIndex] = text1Included
                else:
                    tempCache[colIndex] = text2Included

        for cacheIndex in range(m+1):
            cache[cacheIndex] = tempCache[cacheIndex]

    return cache[m]