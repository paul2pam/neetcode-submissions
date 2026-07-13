class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            if num not in s:
                s.add(num)
            elif num in s:
                s.remove(num)


        return list(s)[0]
