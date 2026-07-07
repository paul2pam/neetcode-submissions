class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if i >= len(prices):
                return 0

            next_day = dfs(i + 1, buying)

            if buying:
                res = max(dfs(i + 1, not buying) - prices[i], next_day)
            if not buying:
                res = max(dfs(i + 2, not buying) + prices[i], next_day)

            dp[(i, buying)] = res
            return res

        return dfs(0, True)