class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        minStack = []
        ans = 0

        for i, h in enumerate(heights):
            start = i
            while minStack and minStack[-1][1]>h:
                start, maxHeight = minStack.pop()
                ans = max(ans, (i-start)*maxHeight)

            minStack.append((start, h))
        
        for i, h in minStack:
            ans = max(ans, h*(n-i))

        return ans