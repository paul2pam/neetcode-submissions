class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def simulate(rate):
            time = 0
            for pile in piles:
                time += -(-pile // rate)
            return time
        
        best = float("INF")

        def binary_search(l , r):
            nonlocal best
            if l > r:
                return
            mid = (l + r) // 2
            n = simulate(mid)

            if n > h:                    
                binary_search(mid + 1, r)
            else:
                best = min(best, mid)
                binary_search(l, mid - 1)

            
                
        
        binary_search(1, max(piles))
        return best