class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reachable = [False] * len(nums)
        reachable[0] = True

        for i in range(len(nums)):
            if (reachable[i] == False):
                return False
            reach = min(i+nums[i]+1, len(nums))

            reachable[i:reach] = [True] * (reach - i)
            
        return True