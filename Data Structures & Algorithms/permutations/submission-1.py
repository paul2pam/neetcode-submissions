class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs (s, arr):
            #print(f"dfs({s},{arr})")
            if len(arr) == len(nums):
                #print(f"we append {arr} to {res}")
                res.append(arr)
                #print(res)
                return
            for num in nums:
                if num not in s:
                    #print(f"{num} not in {s}")
                    s.add(num)
                    arr.append(num)
                    dfs(s, arr.copy())
                    s.remove(num)
                    arr.remove(num)
        s = set()
        dfs(s, [])
        return res
