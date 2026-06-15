class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        s = set()
        grids = []
        def permutations(s, arr):
            
            for i in range(n):
                if i not in s:
                    s_new = s.copy()
                    s_new.add(i)
                    permutations(s_new, arr + [i])
            if (len(arr) == n):
                grids.append(arr)

        permutations(s, [])
        
        def should_remove(grid):
            for i in range(n):
                for j in range(i + 1, n):
                    if grid[i] + (j - i) == grid[j] or \
                    grid[i] - (j - i) == grid[j]:
                        return True
                        
        grids = [grid for grid in grids if not should_remove(grid)]
        print(grids)
        
        def make_board(grid):
            arr = [["."] * n for _ in range(n)]
            for col, row in enumerate(grid):
                arr[col][row] = "Q"
            res = []
            row = ""
            for lst in arr:
                for dot in lst:
                    row = row + dot
                res.append(row)
                row = ""
            return res


        return [make_board(grid) for grid in grids]