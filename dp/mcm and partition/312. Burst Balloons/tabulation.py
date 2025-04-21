class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        cache = [[0 for col in range(len(nums)+2)] for row in range(len(nums)+2)]
        n = len(nums)
        for start in range(n, -2, -1):
            for end in range(start,n+1):
                if end-start<=1:
                    continue
                maxCoins = 0
                for index in range(start+1, end):
                    leftNeighbour = 1 if start<0 else nums[start]
                    rightNeighbour = 1 if end>=len(nums) else nums[end]
                    burst =  leftNeighbour * rightNeighbour * nums[index]
                    currCoins = burst + cache[start+1][index+1] + cache[index+1][end+1]
                    if maxCoins < currCoins:
                        maxCoins = currCoins

                cache[start+1][end+1] = maxCoins        

        return cache[0][len(nums)+1]