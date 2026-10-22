"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_h = []

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            start, end = interval.start, interval.end

            if min_h and min_h[0] <= start:
                heapq.heappop(min_h)
            
            heapq.heappush(min_h, end)
        
        return len(min_h)
            

