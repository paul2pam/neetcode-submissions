class Solution:
    def longestPalindrome(self, s: str) -> str:
        tr = s[0]
        max_len = 1

        for i in range(len(s)):
            l = i
            r = i
            while (l > 0 and r < len(s) - 1):
                l -= 1
                r += 1
                if s[l] != s[r]:
                    break
                if (r - l + 1 > len(tr)):
                    tr = s[l:r+1]

            l = i + 1
            r = i
            while (l > 0 and r < len(s) - 1):
                l -= 1
                r += 1
                if s[l] != s[r]:
                    break
                if (r - l + 1 > len(tr)):
                    tr = s[l:r+1]

        return tr