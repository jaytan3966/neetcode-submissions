class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for l, r in intervals:
            if stack and stack[-1][1]>=l:
                oldL, oldR = stack.pop()
                stack.append([min(oldL, l), max(oldR, r)])
            else:
                stack.append([l,r])
        return stack