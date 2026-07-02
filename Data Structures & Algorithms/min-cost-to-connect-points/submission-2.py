class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        heapq.heappush(h, (0, points[0]))
        seen = set()
        res = 0
        while len(seen) < len(points):
            res_d, point1 = heapq.heappop(h)
            if tuple(point1) in seen:
                continue
            seen.add(tuple(point1))
            res += res_d

            for point2 in points:
                d = abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
                heapq.heappush(h, (d, point2))

        return res


