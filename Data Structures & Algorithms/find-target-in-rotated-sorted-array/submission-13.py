class Solution:
    def findSplit(self, nums: List[int], l:int, r: int) -> int:
        n = (l + r) // 2


        if (r - l == 0):
            return l

        if (nums[n] > nums[n + 1]):
            return n + 1

        if (nums[l] > nums[n]): #if its in the left side
            return self.findSplit(nums, l, n)
        if (nums[r] < nums[n]): #if the split is on the right side
            return self.findSplit(nums, n + 1, r)
        

        return 0 #if the whole thing is sorted

    def findTarget(self, nums, l, r, target):
        n = (l + r) // 2

        if (nums[n] == target):
            return n
        
        if (r - l <= 0):
            return -1

        if (nums[n] > target): #its on the left side
            return self.findTarget(nums, l, n, target)
        if (nums[n] < target): #its on the right side
            return self.findTarget(nums, n + 1, r, target)

    def search(self, nums: List[int], target: int) -> int:

        idx = self.findSplit(nums, 0, len(nums) - 1)
        
        newNums = nums[idx: len(nums)] + nums[0 : idx]
        print(idx)
        print(newNums)

        output = self.findTarget(newNums, 0, len(nums) - 1, target)

        if output == -1:
            return -1
        else:
            return (output + idx) % len(nums)
