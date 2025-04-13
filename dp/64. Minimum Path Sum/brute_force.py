class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        rows, cols = len(grid), len(grid[0])
        return self.helper(rows-1, cols-1, grid)

    def helper(self, row, col, grid) ->int :

        if row == 0 and col == 0:
            return grid[row][col]
        if row < 0 or col < 0:
            return -1

        currentSum = grid[row][col]
        rightTraversalSum = self.helper(row, col-1, grid)
        bottomTraversalSum = self.helper(row-1, col, grid)
        if rightTraversalSum!=-1 and bottomTraversalSum==-1:
            currentSum+=rightTraversalSum
        elif rightTraversalSum==-1 and bottomTraversalSum!=-1:
            currentSum+=bottomTraversalSum
        else:
            currentSum+=min(rightTraversalSum,bottomTraversalSum)
        return currentSum