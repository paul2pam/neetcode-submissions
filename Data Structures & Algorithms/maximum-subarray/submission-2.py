class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        curr = 0
        for num in nums:
            if (curr > 0 and num < 0) or (curr < 0 and num > 0):
                sums.append(curr)
                curr = 0
            curr += num
        sums.append(curr)


        greedy = sums[0]
        curr = sums[0]
        for i in range(1, len(sums)):
            curr = max(curr + sums[i], sums[i])
            greedy = max(greedy, curr)

        for i in nums:
            greedy = max(i, greedy)
        return greedy
                