"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        greatest = max(interval.end for interval in intervals)

        array = [0]*(greatest+1)

        for interval in intervals:
            array[interval.start]+=1
            array[interval.end]-=1

        cur = 0
        for i in range(greatest+1):
            array[i]+=cur
            cur = array[i]
        
        return max(array)