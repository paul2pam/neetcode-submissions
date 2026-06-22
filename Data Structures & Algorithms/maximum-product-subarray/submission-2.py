class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res_max = -float("INF")

        curr_max, curr_min = 1, 1
        for i in range(len(nums)):

            if nums[i] == "0":
                curr_max, curr_min = 1
                continue
            tmp_max = curr_max
            curr_max = max(curr_max * nums[i], curr_min * nums[i], nums[i])
            curr_min = min(curr_min * nums[i], tmp_max * nums[i], nums[i])
            print(nums[i], curr_max, curr_min)
            res_max = max(curr_max, res_max)

        return res_max
