class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(0, 0, triangle)

    def helper(self, row, usedIndex, triangle) -> int:

        if row==len(triangle):
            return 0

        return triangle[row][usedIndex] + min(
            self.helper(row+1, usedIndex, triangle),
            self.helper(row+1, usedIndex+1, triangle)
        )