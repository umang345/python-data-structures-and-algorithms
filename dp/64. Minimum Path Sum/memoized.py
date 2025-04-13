class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for colIndex in range(cols)] for rowIndex in range(rows)]
        return self.helper(rows-1, cols-1, grid, dp)

    def helper(self, row, col, grid, dp) ->int :

        if row == 0 and col == 0:
            return grid[row][col]
        if row < 0 or col < 0:
            return -1

        if dp[row][col]!=-1:
            return dp[row][col]

        currentSum = grid[row][col]
        rightTraversalSum = self.helper(row, col-1, grid,dp)
        bottomTraversalSum = self.helper(row-1, col, grid, dp)
        if rightTraversalSum!=-1 and bottomTraversalSum==-1:
            currentSum+=rightTraversalSum
        elif rightTraversalSum==-1 and bottomTraversalSum!=-1:
            currentSum+=bottomTraversalSum
        else:
            currentSum+=min(rightTraversalSum,bottomTraversalSum)

        dp[row][col] = currentSum
        return currentSum