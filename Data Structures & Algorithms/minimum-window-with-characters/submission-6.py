class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}

        for char in t:
            need[char] = 1 if char not in need else need[char] + 1
            have[char] = 0
        
        l = 0
        r = 0
        currently_satisfied = 0
        need_satisfied = len(need)
        res = ""
        minlen = float("inf")
        for r in range(len(s)):
            if s[r] in have:
                have[s[r]] += 1
                if have[s[r]] == need[s[r]]:
                    currently_satisfied += 1
            
            while currently_satisfied == need_satisfied and l <= r:
                if (r - l + 1 < minlen):
                    minlen = r - l + 1
                    res = s[l:r+1]
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        currently_satisfied -= 1
                l += 1
        
        return res

