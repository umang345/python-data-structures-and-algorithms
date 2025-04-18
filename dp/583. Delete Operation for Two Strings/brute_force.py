class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        lcm = self.helper(n,m,word1, word2)
        return (n+m) - (2*lcm)

    def helper(self, index1, index2, word1, word2) -> int:
        if index1==0 or index2==0:
            return 0

        if word1[index1-1] == word2[index2-1]:
            return 1+self.helper(index1-1, index2-1, word1, word2)
        else:
            return max(
                self.helper(index1-1, index2-1, word1, word2),
                max(
                    self.helper(index1-1, index2, word1, word2),
                    self.helper(index1, index2-1, word1, word2)
                )
            )