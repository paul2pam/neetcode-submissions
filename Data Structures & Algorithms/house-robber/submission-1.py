class Solution:

    #nums[i] -> money in ith house 
    def dfs(self, nums, i):
        if i in self.d:
            return self.d[i]
        elif i >= len(nums):
            return 0
        else:
            self.d[i] = max(nums[i] + self.dfs(nums, i + 2), self.dfs(nums, i + 1))
            return self.d[i]

    #2,9,8,3,6
    def rob(self, nums: List[int]) -> int:
        self.d = {}
        return max(nums[0] + self.dfs(nums, 2), self.dfs(nums, 1))