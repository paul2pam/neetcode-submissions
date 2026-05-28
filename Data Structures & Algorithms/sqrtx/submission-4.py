class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x + 1):
            if i ** 2 == x:
                return i
            if i ** 2 > x:
                return i - 1