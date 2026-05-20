class Solution:
    def countSubstrings(self, s: str) -> int:
        tr = 0
        for i in range(len(s)):
            l = i
            r = i
            while (l >= 0 and r < len(s)):
                if (s[l] != s[r]):
                    break
                tr += 1
                l -= 1
                r += 1
            print(tr)
                
                
            l = i
            r = i + 1
            while (l >= 0 and r < len(s)):
                if (s[l] != s[r]):
                    break
                l -= 1
                r += 1
                tr += 1
            print(tr)

        return tr