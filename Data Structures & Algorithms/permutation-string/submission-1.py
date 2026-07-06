class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        has = {}

        need_count = 0
        has_count = 0
        for char in s1:
            if char not in need:
                need_count += 1
            need[char] = need.get(char, 0) + 1

        for i in range(len(s1)):
            has[s2[i]] = has.get(s2[i], 0) + 1
            if has[s2[i]] == need.get(s2[i], -1):
                has_count += 1
            if has_count == need_count:
                return True
        #print(has, need)
        for i in range(len(s1), len(s2)):
            has[s2[i]] = has.get(s2[i], 0) + 1
            if has[s2[i]] == need.get(s2[i], -1):
                has_count += 1

            j = i - len(s1)
            if has[s2[j]] == need.get(s2[j], -1):
                has_count -= 1
            has[s2[j]] -= 1
            
            
            if has_count == need_count:
                return True
            #print(has, has_count)
        
        return False



