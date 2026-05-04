class Solution:
    def hammingWeight(self, n: int) -> int:
        sn = bin(n)[2:]
        count = 0
        for c in sn:
            if c == "1":
                count += 1
        return count