"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_h = []
        n = len(intervals)

        for i in range(n):
            while min_h and min_h[0] <= intervals[i].end:
                heapq.heappop(min_h)
            heapq.heappush(min_h, intervals[i].end)
        
        return len(min_h)
        
