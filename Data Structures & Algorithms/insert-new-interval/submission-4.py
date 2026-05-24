class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        if newInterval[0] > intervals[-1][1]: #edge case: it goes at the end
            intervals.append(newInterval)
            return intervals
        
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1]:
                newInterval[0] = min(intervals[i][0], newInterval[0])

                if newInterval[1] < intervals[i][0]: #case 1: the end comes before the start
                    intervals.insert(i, newInterval) # we just insert it before
                    return intervals
                
                if newInterval[1] <= intervals[i][1]: # case 2, the end is in the interval
                    intervals[i][0] = newInterval[0] # we just change the front
                    return intervals

                for j in range(i + 1, len(intervals)):
                    
                    if newInterval[1] < intervals[j][0]: #case 3a: the end stops before the next beginning

                        del intervals[i + 1: j] #delete all the intervals we've absorbed
                        intervals[i] = newInterval
                        return intervals
                    if newInterval[1] <= intervals[j][1]: #case 3b: the end stops before the next end

                        newInterval[1] = intervals[j][1]
                        del intervals[i + 1: j + 1]
                        intervals[i] = newInterval
                        return intervals
                print(intervals[i + 1: len(intervals)])
                del intervals[i + 1: len(intervals)]
                
                intervals[i] = newInterval #case 4: the end goes beyond the list
                return intervals
        
        
                    
