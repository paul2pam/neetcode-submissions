class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                l = mid + 1
            if mid ** 2 > x:
                r = mid - 1
        return r
        