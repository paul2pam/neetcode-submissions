class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        def inside(query, interval):
            if query >= interval[0] and query <= interval[1]:
                return True
            return False
        
        intervals = sorted(intervals, key = lambda x: x[1] - x[0])
        print(intervals)

        res = []
        for query in queries:
            flag = False
            for interval in intervals:
                if inside(query, interval):
                    res.append(interval[1] - interval[0] + 1)
                    flag = True
                    break
            if not flag:
                res.append(-1)

        return res
        