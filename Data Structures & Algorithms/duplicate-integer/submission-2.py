class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            if num in m:
                return True
            else:
                m[num] = 1
        return False
