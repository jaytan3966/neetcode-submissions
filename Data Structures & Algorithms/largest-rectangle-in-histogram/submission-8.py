class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        min_stack = []
        ans = 0

        for i, height in enumerate(heights):
            start = i
            while min_stack and min_stack[-1][0] > height:
                    max_h, start = min_stack.pop()
                    ans = max(ans, max_h*(i-start))
            min_stack.append((height, start))
        
        n = len(heights)

        for height, i in min_stack:
            ans = max(ans, height*(n-i))
        print(min_stack)
        return ans

