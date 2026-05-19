class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        

        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(n):
            for j in range(n // 2):
                tmp = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = matrix[i][j]
                matrix[i][j] = tmp
                