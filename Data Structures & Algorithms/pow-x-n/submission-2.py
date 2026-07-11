class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        def helper(x, n, remainder):
            if n == 1:
                return x * remainder
            if n % 2 == 1:
                remainder *= x
                n -= 1
            x = x * x
            n = n / 2
            return helper(x, n, remainder)
        
        if n < 0: 
            x = 1/ x
            n = -n
        return helper(x, n, 1)