"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        prev = None
        n = len(intervals)

        for i in range(n):
            if prev is None:
                prev = intervals[i]
                continue
            
            last_start, last_end = prev.start, prev.end

            if last_start <= intervals[i].start < last_end or last_start <= intervals[i].end < last_end:
                return False
            
            prev = intervals[i]
        return True
