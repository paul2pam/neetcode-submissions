class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        nums = sorted(nums)
        s = sum(nums) / 2
        def dfs(i, total_left):
            if i == len(nums) or nums[i] > total_left:
                return False
            print(f"trying {nums[i]} on {total_left}")

            if nums[i] == total_left:
                return True
            
            else:
                return dfs(i + 1, total_left - nums[i]) or dfs(i + 1, total_left)


        return dfs(0, s)