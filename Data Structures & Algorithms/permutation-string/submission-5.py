class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has = {}
        needs = {}
        for char in s1:
            needs[char] = needs.get(char, 0) + 1
        has_count = 0

        l, r = 0, 0
        while r < len(s2):
            has[s2[r]] = has.get(s2[r], 0) + 1
            if has[s2[r]] == needs.get(s2[r], 0):
                has_count += 1
            if has_count == len(needs):
                return True
            r += 1
            
            while l <= r - len(s1):
                if has[s2[l]] == needs.get(s2[l], 0):
                    has_count -= 1 
                has[s2[l]] -= 1
                l += 1
        return False




