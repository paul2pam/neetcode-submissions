class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def edible(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)
            if res <= h:
                return True
            else:
                return False
        
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            
            if edible(k):
                r = k - 1
            else:
                l = k + 1
        
        return l
            
