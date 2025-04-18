class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        front = s
        back = "".join(list(reversed(s)))
        return n - self.helper(n,n,front, back)
        
    def helper(self, index1, index2, front, back) -> int:
        if index1==0 or index2==0:
            return 0

        if front[index1-1]==back[index2-1]:
            return 1+self.helper(index1-1, index2-1, front, back)
        else:
            return max(
                self.helper(index1-1, index2-1, front, back),
                max(
                    self.helper(index1-1, index2, front, back),
                    self.helper(index1, index2-1, front, back)
                )
            )