class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def recurse(i, j):
            if j >= len(t):
                dp[(i, j)] = 1
                #print(f"{i, j} produced {dp[(i, j)]}")
                return dp[(i, j)]

            if i >= len(s):
                dp[(i, j)] = 0
                return dp[(i, j)]
            
            if (i, j) in dp:
                #print(f"{i, j} produced {dp[(i, j)]} due to dp")
                return dp[(i, j)]

            if s[i] != t[j]:
                #print(f"trying {i + 1, j} now")
                dp[(i, j)] = recurse(i + 1, j)
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = recurse(i + 1, j + 1) + recurse(i + 1, j)
                return dp[(i, j)]

            

        return recurse(0, 0)