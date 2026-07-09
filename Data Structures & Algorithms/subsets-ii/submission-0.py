class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        s = set()

        nums = sorted(nums)
        res = []

        def recurse(i, arr):
            if i >= len(nums):
                return
            
            if tuple(arr) not in s:
                s.add(tuple(arr))
                res.append(tuple(arr))
            recurse(i + 1, arr)

            new_arr = arr + [nums[i]]
            if tuple(new_arr) not in s:
                s.add(tuple(new_arr))
                res.append(tuple(new_arr))
            recurse(i + 1, new_arr)

        recurse(0, [])
        return res