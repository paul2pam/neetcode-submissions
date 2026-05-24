class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = [False] * m
        cols = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if cols[j]:
                    matrix[i][j] = 0
                if rows[i]:
                    matrix[i][j] = 0
                




        
        

        
        