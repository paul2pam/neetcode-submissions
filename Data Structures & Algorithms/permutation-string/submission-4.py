class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        r = len(s1)
        while r <= len(s2):
            l = r - len(s1)
            if sorted(s2[l:r]) == s1:
                return True
            r += 1
        
        return False