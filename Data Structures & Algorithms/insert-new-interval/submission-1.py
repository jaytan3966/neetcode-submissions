class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        i = 0
        for x,y in intervals:
            if newInterval[1]<x:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > y:
                ans.append([x,y,])
            else:
                newInterval[0], newInterval[1] = min(newInterval[0], x), max(newInterval[1], y)
            i+=1
        ans.append(newInterval)
        return ans
