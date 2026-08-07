class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(k):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] > 1:
                return True
        for j in range(k, len(nums)):
            i = j - k - 1
            if i >= 0:
                #print(i, d[nums[i]])
                d[nums[i]] -= 1
            if d.get(nums[j], 0) > 0:
                #print(d, j)
                return True
            d[nums[j]] = d.get(nums[j], 0) + 1
        return False
            
            