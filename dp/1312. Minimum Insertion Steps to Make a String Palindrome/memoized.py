class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        front = s
        back = "".join(list(reversed(s)))
        cache = [[-1 for colInde in range(n+1)] for rowIndex in range(n+1)]
        return n - self.helper(n,n,front, back, cache)
        
    def helper(self, index1, index2, front, back, cache:list) -> int:
        if index1==0 or index2==0:
            return 0

        if cache[index1][index2]!=-1:
            return cache[index1][index2]

        if front[index1-1]==back[index2-1]:
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