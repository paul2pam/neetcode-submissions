class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        def find_substring(i):

            j = bound = i
            
            while j < len(s) and counts[s[i]] > 0:
                
                if s[j] != s[i] and counts[s[j]] > 0:
                    bound = max(j, find_substring(j))
                else:
                    counts[s[j]] -= 1
                j += 1
            return max(bound, j)

        res = []
        for i in range(len(s)):
            if counts[s[i]] > 0:
                j = find_substring(i)
                res.append(j - i)
                i = j
        return res
                