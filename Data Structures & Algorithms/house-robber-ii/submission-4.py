class Solution:
    def rob(self, nums: List[int]) -> int:

        tr = nums[0]

        nums1 = nums[1:]
        mem = [0] * len(nums1)

        for i in range(len(nums1)):
            prev1 = prev2 = 0
            if (i - 2 >= 0):
                prev1 = mem[i - 2]
            if (i - 3 >= 0):
                prev2 = mem[i - 3]
            
            prev = max(prev1, prev2)

            mem[i] = max(nums1[i], nums1[i] + prev)
            tr = max(tr, mem[i])


        nums2 = nums[:-1]
        mem2 = [0] * len(nums2)

        for i in range(len(nums2)):
            prev1 = prev2 = 0
            if (i - 2 >= 0):
                prev1 = mem2[i - 2]
            if (i - 3 >= 0):
                prev2 = mem2[i - 3]

            prev = max(prev1, prev2)

            mem2[i] = max(nums2[i], nums2[i] + prev)
            tr = max(tr, mem2[i])

        return tr
