class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def sums_to_target(subset, curr_sum, i):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum > target or i == len(candidates):
                return
            
            #we include current one
            sums_to_target(subset + [candidates[i]], curr_sum + candidates[i], i + 1)

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            sums_to_target(subset.copy(), curr_sum, i + 1)

        sums_to_target([], 0, 0)
        return res