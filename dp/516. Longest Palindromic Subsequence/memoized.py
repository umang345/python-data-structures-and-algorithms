class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        cache = [[-1 for colIndex in range(n+1)] for colIndex in range(n+1)]
        return self.helper(len(s), len(s), s, "".join(list(reversed(s))), cache)

    def helper(self,index1, index2, front, back, cache:list) -> int:
        if index1==0 or index2==0:
            return 0

        if cache[index1][index2]!=-1:
            return cache[index1][index2]

        if front[index1-1] == back[index2-1]:
            cache[index1][index2] = 1+self.helper(index1-1, index2-1, front, back, cache)
        else:
            cache[index1][index2] = max(
                self.helper(index1-1, index2-1, front, back, cache),
                max(
                    self.helper(index1-1, index2, front, back, cache),
                    self.helper(index1, index2-1, front, back, cache)
                )
            )
        
        return cache[index1][index2]