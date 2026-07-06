class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []

        curr = -float("INF")
        for i in range(k):
            curr = max(curr, nums[i])
            heapq.heappush(h, (-nums[i], i))
        res.append(curr)
        print(f"h: {h}")
        for i in range(k, len(nums)):
            heapq.heappush(h, (-nums[i], i))
            while h[0][1] <= i - k:
                heapq.heappop(h)
            
            res.append(-h[0][0])

        return res
            
