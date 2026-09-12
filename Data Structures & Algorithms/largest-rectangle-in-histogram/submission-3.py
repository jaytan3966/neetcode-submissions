class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index)*height)
                i = index
            stack.append((i, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h*(n-i))
        return maxArea