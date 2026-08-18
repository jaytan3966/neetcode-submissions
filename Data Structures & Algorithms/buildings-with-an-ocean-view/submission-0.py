class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        ans = []
        n = len(heights)

        stack = []
        for i in range(n-1, -1, -1):
            
            while stack and stack[-1]<heights[i]:
                stack.pop()
            if not stack or stack[-1]<heights[i]:
                ans.append(i)
            stack.append(heights[i])

        ans.sort()
        return ans