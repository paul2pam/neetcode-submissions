class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i_sum = 0
        for i in range(len(nums) + 1):
            i_sum += i
        num_sum = 0
        for num in nums:
            num_sum += num
        return i_sum - num_sum
