class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = {i : [] for i in range(n)}
        for flight in flights:
            d[flight[0]].append((flight[1], flight[2]))
        print(d)


        def dfs(src, cost, flights_left):

            if (src, flights_left) in dp:
                return dp[(src, flights_left)] + cost
            if flights_left == 0:
                
                return float("INF")
            
            dp[(src, flights_left)] = float("INF")
            for flight in d[src]:
                res = dfs(flight[0], cost + flight[1], flights_left - 1)
                dp[(src, flights_left)] = min(res, dp[(src, flights_left)])
            return dp[(src, flights_left)]

        dp = {}
        for i in range(k + 1):
            dp[(dst, i)] = 0
        res = dfs(src, 0, k+1)
        
        if res == float("INF"):
            return -1
        else:
            return res
        
