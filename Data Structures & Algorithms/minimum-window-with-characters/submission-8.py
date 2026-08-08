class Solution:
    def minWindow(self, s: str, t: str) -> str:
        has = {}
        needs = {}
        
        has_count = 0
        needs_count = 0
        for char in t:
            if needs.get(char, 0) == 0:
                needs_count += 1
            needs[char] = needs.get(char, 0) + 1
        print(has, needs)

        r, l = 0, 0
        min_len = len(s)
        res = ""

        while r < len(s): 
            has[s[r]] = has.get(s[r], 0) + 1
            if has[s[r]] == needs.get(s[r], 0):
                has_count += 1
            r += 1

            #print(has_count, has)
            while l < r and has_count == needs_count:
                has[s[l]] = has.get(s[l], 0) - 1
                if has[s[l]] == needs.get(s[l], 0) - 1:
                    has_count -= 1
                if r - l <= min_len:
                    res = s[l:r]
                    min_len = r - l
                l += 1
                

        return res
