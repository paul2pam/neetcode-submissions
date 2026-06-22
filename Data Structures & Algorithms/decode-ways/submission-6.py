class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}

        def count_ways(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if s[i] == "1" and i < len(s) - 1:
                dp[i] = count_ways(i + 1) + count_ways(i + 2)
                return dp[i]
            if s[i] == "2":
                if i < len(s) - 1 and s[i + 1] != "9" and s[i + 1] != 8 and s[i + 1] != "7":
                    return count_ways(i + 1) + count_ways(i + 2)
            dp[i] = count_ways(i + 1)
            return count_ways(i + 1)

        return count_ways(0)

