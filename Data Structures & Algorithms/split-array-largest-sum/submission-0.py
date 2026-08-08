class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def splittable(max_sum):
            running_sum = 0
            buckets = 1
            for num in nums:
                if running_sum + num > max_sum:
                    running_sum = 0
                    buckets += 1
                running_sum += num
            return buckets

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2
            if splittable(mid) <= k:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
