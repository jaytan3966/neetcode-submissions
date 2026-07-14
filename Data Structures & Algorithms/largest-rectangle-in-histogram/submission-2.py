class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        right = [n]*n

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        ans = 0
        for i in range(n):
            left[i]+=1
            right[i]-=1
            ans = max(ans, heights[i] * (right[i]-left[i]+1))
        return ans