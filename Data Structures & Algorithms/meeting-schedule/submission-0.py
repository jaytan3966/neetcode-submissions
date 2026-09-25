"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last = None

        for interval in intervals:
            start, end = interval.start, interval.end
            if last and (last[0]<=start<=last[1] or last[0]<=end<=last[1]):
                return False
            last = (start, end)
        return True