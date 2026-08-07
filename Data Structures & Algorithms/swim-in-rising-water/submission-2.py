class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        h = []
        heapq.heappush(h, (grid[0][0], 0, 0))
        vis = set()

        highest = grid[0][0]
        while h:
            curr = heapq.heappop(h)
            highest = max(highest, curr[0])
            #print(h, highest)

            if (curr[1], curr[2]) in vis:
                continue
            vis.add((curr[1], curr[2]))

            if (curr[1], curr[2]) == (len(grid) - 1, len(grid[0]) - 1):
                return highest
            
            for direction in directions: 
                i = curr[1] + direction[0]
                j = curr[2] + direction[1]
                #print(direction, i, j)
                if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and (i, j) not in vis:
                    heapq.heappush(h, (grid[i][j], i, j))
                    #print("added")
                    #print("not added")
                
            
        
        return highest
                

        