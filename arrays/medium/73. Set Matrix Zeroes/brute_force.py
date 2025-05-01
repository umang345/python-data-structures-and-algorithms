class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowCount, colCount = len(matrix), len(matrix[0])
        
        rowTrack = [1]*rowCount 
        colTrack = [1]*colCount

        for row in range(rowCount):
            for col in range(colCount):
                if matrix[row][col] == 0:
                    rowTrack[row] = 0
                    colTrack[col] = 0

        # Mark rows as 0

        for row in range(rowCount):
            if rowTrack[row] == 0:
                for index in range(colCount):
                    matrix[row][index] = 0
        
        #  Mark cols as 0

        for col in range(colCount):
            if colTrack[col] == 0:
                for index in range(rowCount):
                    matrix[index][col] = 0

'''
TC   O(3*m*n)
SC    O(m+n)
'''