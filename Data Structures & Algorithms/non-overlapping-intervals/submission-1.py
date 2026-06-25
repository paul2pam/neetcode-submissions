class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        res = 0
        prevend = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] < prevend:
                res += 1
                prevend = intervals[i][1]
                continue
            if intervals[i][0] < prevend:
                res += 1
                continue
            else:
                prevend = intervals[i][1]
        return res