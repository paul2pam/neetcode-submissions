class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subset(nums, i, curr):
            if i == len(nums):
                res.append(curr)
                return
            doesnt_include = curr.copy()
            subset(nums, i + 1, doesnt_include)

            includes = curr.copy()
            includes.append(nums[i])
            subset(nums, i + 1, includes)


        curr = []
        subset(nums, 0, curr)

        return res