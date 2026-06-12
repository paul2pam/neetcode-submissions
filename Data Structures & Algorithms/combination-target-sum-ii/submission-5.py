class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def sums_to_target(subset, curr_sum, i):
            if curr_sum == target:
                res.append(subset.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + curr_sum > target:
                    break
                subset.append(candidates[j])
                sums_to_target(subset, curr_sum + candidates[j], j + 1)
                subset.pop()

        sums_to_target([], 0, 0)
        return res