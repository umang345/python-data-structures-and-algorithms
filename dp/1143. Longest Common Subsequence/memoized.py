class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1 for colIndex in range(len(text2)+1)] for rowIndex in range(len(text1)+1)]
        return self.helper(len(text1), len(text2), text1, text2, cache)

    def helper(self,index1, index2, text1, text2, cache:list[int]) -> int:
        if index1==0 or index2==0:
            return 0

        if cache[index1][index2]!=-1:
            return cache[index1][index2]

        if text1[index1-1]==text2[index2-1]:
            cache[index1][index2] = 1+self.helper(index1-1, index2-1, text1, text2,cache)
        else:
            cache[index1][index2] = max(
                self.helper(index1-1, index2-1, text1, text2,cache),
                max(
                    self.helper(index1-1, index2, text1, text2, cache),
                    self.helper(index1, index2-1, text1, text2, cache)
                )
            )

        return cache[index1][index2]