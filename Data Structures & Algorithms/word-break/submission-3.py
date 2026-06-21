class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = set()
        def helper(i):
            if i in dp:
                return False
            if i >= len(s):
                return True

            for j in range(i, len(s) + 1):
                if s[i:j] in words:
                    if helper(j):
                        return True
            dp.add(i)
            return False


        return helper(0)
