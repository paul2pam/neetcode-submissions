class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        res = 0
        def dfs(curr, i):
            nonlocal res
            if i == len(nums):
                dp[(curr, i)] = 0
                if curr == target:
                    dp[(curr, i)] += 1
                    res += 1
                return

            if (curr - nums[i], i + 1) in dp:
                res += dp[(curr - nums[i], i + 1)]
            else:
                dfs(curr - nums[i], i + 1)

            if (curr + nums[i], i + 1) in dp:
                res += dp[(curr + nums[i], i + 1)]
            else:
                dfs(curr + nums[i], i + 1)


        dfs(0, 0)
        return res