class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for char in s:
            if char not in s_d:
                s_d[char] = 1
            else:
                s_d[char] += 1
        t_d = {}
        for char in t:
            if char not in t_d:
                t_d[char] = 1
            else:
                t_d[char] += 1
        if s_d == t_d:
            return True
        else:
            return False

        