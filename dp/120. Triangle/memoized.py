class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(0, 0, triangle, dict())

    def helper(self, row, usedIndex, triangle, mem) -> int:

        if row==len(triangle):
            return 0

        key = f"{row}-_-{usedIndex}"
        if not mem.get(key) is None:
            return mem[key]

        mem[key] =  triangle[row][usedIndex] + min(
            self.helper(row+1, usedIndex, triangle, mem),
            self.helper(row+1, usedIndex+1, triangle, mem)
        )

        return mem[key]