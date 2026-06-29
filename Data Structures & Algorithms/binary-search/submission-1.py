class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            print(l, r)
            i = (l + r) // 2
            print(i)
            
            if (nums[i] == target):
                return i
            if l >= r:
                return -1
            if nums[i] < target:
                return binary_search(i + 1, r)
            elif nums[i] > target:
                return binary_search(l, i-1)
            

        return binary_search(0, len(nums) - 1)