class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)

        stack = [n-1]

        for i in range(n-2, -1, -1):
            if heights[stack[-1]]<heights[i]:
                stack.append(i)
        stack.reverse()
        return stack