class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l, r = 0, 0
        st = set()

        while r < len(s):
            while l < r and s[r] in st:
                st.discard(s[l])
                l += 1
            
            st.add(s[r])
            r += 1
            res = max(res, r - l)
            
        
        return res