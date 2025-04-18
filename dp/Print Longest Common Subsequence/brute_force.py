def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    return helper(n,m,s1,s2)

def helper(index1:int, index2:int, text1:str, text2:str) -> str:
    if index1==0 or index2==0:
        return ""

    if text1[index1-1] == text2[index2-1]:
        # print("Here")
        return text1[index1-1]+helper(index1-1, index2-1, text1, text2)
    else:
        neitherIncluded = helper(index1-1, index2-1, text1, text2)
        text1Included = helper(index1-1, index2, text1, text2)
        text2Included = helper(index1, index2-1, text1, text2)

        if len(neitherIncluded) >= len(text1Included) and len(neitherIncluded) >= len(text2Included):
            return neitherIncluded
        elif len(text1Included) >= len(neitherIncluded) and len(text1Included) >= len(text2Included):
            return text1Included
        else:
            return text2Included
        
# print(findLCS(5,6,"ababa","cbbcad"))