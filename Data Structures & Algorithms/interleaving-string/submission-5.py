class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if k >= len(s3):
                dp[(i, j, k)] = i >= len(s1) and j >= len(s2)
                return dp[(i,j,k)]
                
            if i < len(s1) and s1[i] == s3[k]:
                dp[(i + 1, j, k)] = dfs(i + 1, j, k + 1)
                if dp[(i + 1, j, k)]:
                    return True
                
            if j < len(s2) and s2[j] == s3[k]:
                dp[(i, j + 1, k)]  = dfs(i, j + 1, k + 1)
                if dp[(i, j + 1, k)]:
                    return True

            dp[(i, j, k)] = False
            return False

        return dfs(0, 0, 0)