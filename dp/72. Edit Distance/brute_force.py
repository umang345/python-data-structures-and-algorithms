class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        return self.helper(n,m,word1, word2)

    def helper(self, index1, index2, word1,word2) -> int:
        if index1==0:
            return index2
        if index2==0:
            return index1

        if word1[index1-1]==word2[index2-1]:
            return self.helper(index1-1, index2-1,word1, word2)
        else:
            return 1+min(
                self.helper(index1-1, index2, word1, word2),
                min(
                    self.helper(index1, index2-1, word1, word2),
                    self.helper(index1-1, index2-1, word1, word2),
                )
            )