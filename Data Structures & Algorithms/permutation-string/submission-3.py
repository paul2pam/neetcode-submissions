class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        r = len(s1)
        while r <= len(s2):
            l = r - len(s1)
            if sorted(s2[l:r]) == sorted(s1):
                return True
            r += 1
        
        return False