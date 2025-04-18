def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    cache = [["" for colIndex in range(m+1)] for rowIndex in range(n+1)]
    
    for rowIndex in range(1, n+1):
        for colIndex in range(1, m+1):

            if s1[rowIndex-1] == s2[colIndex-1]:
                cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex-1] + s1[rowIndex-1]
            else:
                neitherIncluded = cache[rowIndex-1][colIndex-1]
                text1Included = cache[rowIndex-1][colIndex]
                text2Included = cache[rowIndex][colIndex-1]

                if len(neitherIncluded) >= len(text1Included) and len(neitherIncluded) >= len(text2Included):
                    cache[rowIndex][colIndex] = neitherIncluded
                elif len(text1Included) >= len(neitherIncluded) and len(text1Included) >= len(text2Included):
                    cache[rowIndex][colIndex] = text1Included
                else:
                    cache[rowIndex][colIndex] = text2Included

    return cache[n][m]