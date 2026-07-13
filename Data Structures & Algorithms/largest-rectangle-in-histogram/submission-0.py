class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        left, right = [0]*n, [n]*n
        ans = 0

        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            left[i]+=1
            right[i]-=1
            ans = max(ans, (right[i]-left[i]+1)*heights[i])
        return ans

            
