class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0 #s index 
        j = 0 #p index 

        dp = {}

        #at every j, check if there is a *, this is our split
        def check(i, j):
            print(f"checking {(i, j)}")
            res = False
            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(p):
                res = (i == len(s))
                print(f"res: {res}")
            else:
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    
                if j + 1 < len(p) and p[j + 1] == '*':
                    res = check(i, j + 2) or (match and check(i + 1, j))
                else:
                    res = match and check(i + 1, j + 1)

            dp[(i, j)] = res
            return res

        return check(0, 0)
    