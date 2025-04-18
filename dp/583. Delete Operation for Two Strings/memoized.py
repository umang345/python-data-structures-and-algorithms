class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        cache = [[-1 for colIndex in range(m+1)] for rowIndex in range(n+1)]
        lcm = self.helper(n,m,word1, word2, cache)
        return (n+m) - (2*lcm)

    def helper(self, index1, index2, word1, word2, cache) -> int:
        if index1==0 or index2==0:
            return 0

        if cache[index1][index2]!=-1:
            return cache[index1][index2]

        if word1[index1-1] == word2[index2-1]:
            cache[index1][index2] = 1+self.helper(index1-1, index2-1, word1, word2, cache)
        else:
            cache[index1][index2] = max(
                self.helper(index1-1, index2-1, word1, word2, cache),
                max(
                    self.helper(index1-1, index2, word1, word2, cache),
                    self.helper(index1, index2-1, word1, word2, cache)
                )
            )
        
        return cache[index1][index2]