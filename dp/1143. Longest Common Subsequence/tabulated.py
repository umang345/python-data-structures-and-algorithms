class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0 for colIndex in range(len(text2)+1)] for rowIndex in range(len(text1)+1)]
        
        for index1 in range(1, len(text1)+1):
            for index2 in range(1, len(text2)+1):
                if text1[index1-1] == text2[index2-1]:
                    cache[index1][index2] = 1+cache[index1-1][index2-1]
                else:
                    cache[index1][index2] = max(
                        cache[index1-1][index2-1],
                        max(
                            cache[index1-1][index2],
                            cache[index1][index2-1]
                        )
                    )

        return cache[len(text1)][len(text2)]