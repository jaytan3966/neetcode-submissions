class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []

        intervals.sort()

        for x,y in intervals:
            if not stack or stack[-1][1]<x:
                stack.append([x,y])
            else:
                oldX, oldY = stack.pop()
                stack.append([min(x,oldX), max(y, oldY)])
        return stack
            
                