class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        seen = set()

        h = [(0, 0, 0)]
        res = 0
        while h:
            effort, i, j = heapq.heappop(h)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            res = max(res, effort)
            if (i, j) == (len(heights) - 1, len(heights[i]) - 1):
                return res
            if (i - 1, j) not in seen and i - 1 >= 0:
                heapq.heappush(h, (max(res, abs(heights[i][j] - heights[i-1][j])), i - 1, j))
            if (i, j - 1) not in seen and j - 1 >= 0:
                heapq.heappush(h, (max(res, abs(heights[i][j] - heights[i][j-1])), i, j - 1))
            if (i + 1, j) not in seen and i + 1 < len(heights):
                heapq.heappush(h, (max(res, abs(heights[i][j] - heights[i+1][j])), i + 1, j))
            if (i, j + 1) not in seen and j + 1 < len(heights[i]):
                heapq.heappush(h, (max(res, abs(heights[i][j] - heights[i][j+1])), i, j + 1))
            
            #res = max(res, effort)
        return res
        

