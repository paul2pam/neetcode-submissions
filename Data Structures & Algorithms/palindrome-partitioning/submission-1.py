class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = {}
        
        def is_palindrome(substr):
            if len(substr) == 0:
                return False
            
            if substr in dp:
                return dp[substr]

            dp[substr] = True

            for i in range(len(substr) // 2):
                if substr[i] != substr[-i - 1]:
                    dp[substr] = False

            return dp[substr]
        
        res = []

        def check(arr, substr, i):
            if i >= len(s):
                if is_palindrome(substr):
                    #print(arr, substr, res)
                    arr.append(substr)
                    res.append(arr)
                    #print(arr, res)
                return

            new_substr = substr + s[i]
            new_arr = arr.copy()
            
            if is_palindrome(new_substr):
                new_arr.append(new_substr)
                check(new_arr, "", i + 1)

            old_arr = arr.copy()
            check(old_arr, new_substr, i + 1)


        check([], "", 0)

        return res