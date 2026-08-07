class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l = 0
        running_sum = 0
        res = len(nums)
        for r in range(len(nums)):
            
            running_sum += nums[r]
            while running_sum >= target and l <= r: 
                running_sum -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return res