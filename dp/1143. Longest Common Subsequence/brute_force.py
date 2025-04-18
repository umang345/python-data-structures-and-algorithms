class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(len(text1), len(text2), text1, text2)

    def helper(self,index1, index2, text1, text2) -> int:
        if index1==0 or index2==0:
            return 0
        if text1[index1-1]==text2[index2-1]:
            return 1+self.helper(index1-1, index2-1, text1, text2)
        else:
            return max(
                self.helper(index1-1, index2-1, text1, text2),
                max(
                    self.helper(index1-1, index2, text1, text2),
                    self.helper(index1, index2-1, text1, text2)
                )
            )