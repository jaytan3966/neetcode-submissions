class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []

        intervals.append(newInterval)
        intervals.sort()

        for x,y in intervals:
            if stack and stack[-1][1]>=x:
                old_x, old_y = stack.pop()
                stack.append([min(x,old_x), max(y, old_y)])
            else:
                stack.append([x,y])
        return stack