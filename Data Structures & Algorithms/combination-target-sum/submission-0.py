class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def sums_to_target(subset, curr_sum, i):
            if curr_sum + nums[i] > target:
                return
            elif curr_sum + nums[i] == target:
                sub = subset.copy()
                sub.append(nums[i])
                res.append(sub)
            else:
                sub = subset.copy()
                sub.append(nums[i])
                curr_sum += nums[i]
                for j in range(i, len(nums)):
                    sums_to_target(sub, curr_sum, j)
        
        subset = []
        for i in range(len(nums)):
            sums_to_target(subset, 0, i)

        return res
