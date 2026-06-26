class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        
        def helper(n):
            print(n)
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n = n // 10
            print(f"res: {res}")
            if res == 1:
                return True
            if res in d:
                return False
            d.add(res)
            return helper(res)

        return helper(n)
            
            
