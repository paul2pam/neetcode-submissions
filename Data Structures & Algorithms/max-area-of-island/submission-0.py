class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        def area(i, j):
            if (i,j) in seen:
                return 0
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return 0
            if grid[i][j] == 1:
                seen.add((i, j))
                
                return 1 + area(i + 1, j) + area(i, j + 1) + area(i - 1, j) + area (i, j - 1)
                seen.remove((i, j))
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ar = area(i, j)
                    print(res, ar)
                    res = max(res, ar)
                    
        
        return res
            
