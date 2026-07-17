class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()

        def bfs(i, j, dist):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or grid[i][j] < dist:
                return
            if (i, j) in seen:
                return
            seen.add((i, j))
            grid[i][j] = dist

            bfs(i + 1, j, dist + 1)
            bfs(i, j + 1, dist + 1)
            bfs(i - 1, j, dist + 1)
            bfs(i, j - 1, dist + 1)

            seen.remove((i, j))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    bfs(i, j, 0)
        
        
