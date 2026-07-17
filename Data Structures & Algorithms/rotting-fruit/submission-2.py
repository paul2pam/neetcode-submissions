class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        seen = set()
        fresh = grid.copy()
        for i in range(len(fresh)):
            for j in range(len(fresh[i])):
                if fresh[i][j] == 1:
                    fresh[i][j] = float("INF")
                if fresh[i][j] == 2:
                    fresh[i][j] = -1

        def bfs(i, j, time):
            #first 4 conditionals for bounds, then checking if we've explored better already, then not going through 2s or 0s
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or (i, j) in seen or fresh[i][j] == 0:
                return
            if time >= grid[i][j] and grid[i][j] != -1:
                return
            fresh[i][j] = min(time, fresh[i][j])
            

            seen.add((i, j))
            bfs(i+1, j, time + 1)
            bfs(i-1, j, time + 1)
            bfs(i, j+1, time + 1)
            bfs(i, j-1, time + 1)
            seen.remove((i,j))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if fresh[i][j] == -1:
                    bfs(i, j, 0)
        print(fresh)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if fresh[i][j] == float("INF"):
                    return -1
                res = max(res, fresh[i][j])

        return res
