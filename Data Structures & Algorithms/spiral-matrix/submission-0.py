class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        row_min = 0
        row_max = len(matrix) - 1

        col_min = 0
        col_max = len(matrix[0]) - 1

        i = 0
        j = 0

        elements = []
        elements.append(matrix[0][0])
        print(row_min, row_max, col_min, col_max)
        while (len(elements) < len(matrix) * len(matrix[0])):
            while (j < col_max):
                j += 1
                elements.append(matrix[i][j])
                
            if (len(elements) == len(matrix) * len(matrix[0])):
                break

            row_min += 1

            while (i < row_max):
                i += 1
                elements.append(matrix[i][j])

            if (len(elements) == len(matrix) * len(matrix[0])):
                break
                
            col_max -= 1

            while (j > col_min):
                j -= 1
                elements.append(matrix[i][j])
            if (len(elements) == len(matrix) * len(matrix[0])):
                break
                
            row_max -= 1

            while (i > row_min):
                i -= 1
                elements.append(matrix[i][j])
            if (len(elements) == len(matrix) * len(matrix[0])):
                break
                
            col_min += 1

            print(row_min, row_max, col_min, col_max)


        return elements
