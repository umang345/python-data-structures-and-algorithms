class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        cache = [[-1 for colIndex in range(m+1)] for index in range(n+1)]
        return self.helper(n,m,word1, word2, cache)

    def helper(self, index1, index2, word1,word2, cache) -> int:
        if index1==0:
            return index2
        if index2==0:
            return index1

        if cache[index1][index2]!=-1:
            return cache[index1][index2]

        if word1[index1-1]==word2[index2-1]:
            cache[index1][index2] = self.helper(index1-1, index2-1,word1, word2,cache)
        else:
            cache[index1][index2] = 1+min(
                self.helper(index1-1, index2, word1, word2,cache),
                min(
                    self.helper(index1, index2-1, word1, word2,cache),
                    self.helper(index1-1, index2-1, word1, word2,cache),
                )
            )
        
        return cache[index1][index2]