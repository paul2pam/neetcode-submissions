class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        last_popped = 0
        for i in range (n // 2):
            if len(nums1) == 0:
                last_popped = heapq.heappop(nums2)
            elif len(nums2) == 0:
                last_popped = heapq.heappop(nums1)
            elif nums1[0] < nums2[0]:
                last_popped = heapq.heappop(nums1)
            else: 
                last_popped = heapq.heappop(nums2)
            print(last_popped)

        if n % 2 == 1:
            if len(nums1) == 0:
                return nums2[0]
            if len(nums2) == 0:
                return nums1[0]
            return min(nums1[0], nums2[0])
        else:
            if len(nums1) == 0:
                return (last_popped + nums2[0]) / 2
            if len(nums2) == 0:
                return (last_popped + nums1[0]) / 2
            return (last_popped + min(nums1[0], nums2[0])) / 2

        
