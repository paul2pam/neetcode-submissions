"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [(interval.start, "s") for interval in intervals]
        ends = [(interval.end, "e") for interval in intervals]
        times = starts + ends
        times = sorted(times)
        rooms = 0
        res = 0
        for i, time in enumerate(times):
            if time[1] == "s":
                rooms += 1
            if time[1] == "e":
                rooms -= 1
            res = max(res, rooms)
        return res

        
            

