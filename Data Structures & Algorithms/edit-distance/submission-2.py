class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(word1) or j >= len(word2):
                if i >= len(word1) and j >= len(word2):
                    dp[(i, j)] = 0
                elif i >= len(word1):
                    dp[(i, j)] = 1 + dfs(i, j + 1)
                elif j >= len(word2):
                    dp[(i, j)] = 1 + dfs(i + 1, j)
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            
            if word1[i] != word2[j]:
                dp[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
            
            return dp[(i, j)]

        return dfs(0, 0)
        
            