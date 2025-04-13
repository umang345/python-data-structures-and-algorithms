class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<0:
            return 0
        if n==0 or n==1:
            return 1

        prev, curr = 1,1

        for index in range(2, n+1):
            updated = prev+curr
            prev = curr
            curr = updated

        return curr