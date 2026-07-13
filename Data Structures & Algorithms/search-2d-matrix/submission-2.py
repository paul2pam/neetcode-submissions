class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def find_row(l, r):
            
            if r < l:
                return -1
            #print(l, r)
            i = (l + r) // 2
            #print(i)
            if target < matrix[i][0]:
                i = find_row(l, i - 1)

            elif target > matrix[i][-1]:
                i = find_row(i + 1, r)
            
            return i

        i = find_row(0, m - 1)
        if i == -1:
            #print("target wasn't in bounds")
            return False
        row = matrix[i]

        def binary_search(l, r):
            print(l, r)
            if r < l:
                #print(f"{r} < {l}")
                return False
            i = (l + r) // 2
            if target < row[i]:
                return binary_search(l, i - 1)
            elif target > row[i]:
                return binary_search(i + 1, r)
            else:
                return True

        return binary_search(0, n - 1)


        

        
        


        