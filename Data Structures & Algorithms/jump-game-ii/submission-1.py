class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float("INF")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                dp[i] = min(dp[i], dp[j])
            dp[i] += 1

        print(dp)
        return dp[0]