class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()

        def bfs(r, c, prevheight, visited):
            if (r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0])
                or heights[r][c] < prevheight or (r,c) in visited): 
                return 
            visited.add((r,c))
            bfs(r + 1, c, heights[r][c], visited)
            bfs(r, c + 1, heights[r][c], visited)
            bfs(r - 1, c, heights[r][c], visited)
            bfs(r, c - 1, heights[r][c], visited)
                    
        for i in range(len(heights[0])):
            bfs(0, i, heights[0][i], pac)
            bfs(len(heights) - 1, i, heights[len(heights)-1][i], atl)

        for i in range(len(heights)):
            bfs(i, 0, heights[i][0], pac)
            bfs(i, len(heights[0]) - 1, heights[i][len(heights[0]) - 1], atl)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res