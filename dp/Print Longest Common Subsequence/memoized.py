def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    cache = [[None for colIndex in range(m+1)] for rowIndex in range(n+1)]
    return helper(n,m,s1,s2, cache)

def helper(index1:int, index2:int, text1:str, text2:str, cache:list) -> str:
    if index1==0 or index2==0:
        return ""

    if not cache[index1][index2] is None:
        return cache[index1][index2]

    if text1[index1-1] == text2[index2-1]:
        cache[index1][index2] = helper(index1-1, index2-1, text1, text2,cache) + text1[index1-1]
    else:
        neitherIncluded = helper(index1-1, index2-1, text1, text2,cache)
        text1Included = helper(index1-1, index2, text1, text2,cache)
        text2Included = helper(index1, index2-1, text1, text2,cache)

        if len(neitherIncluded) >= len(text1Included) and len(neitherIncluded) >= len(text2Included):
            cache[index1][index2] = neitherIncluded
        elif len(text1Included) >= len(neitherIncluded) and len(text1Included) >= len(text2Included):
            cache[index1][index2] = text1Included
        else:
            cache[index1][index2] = text2Included

    return cache[index1][index2]