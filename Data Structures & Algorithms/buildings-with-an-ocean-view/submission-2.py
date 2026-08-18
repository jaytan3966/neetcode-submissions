class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)

        arr = [False for i in range(n)]
        stack = []

        for i in range(n-1, -1, -1):
            if stack and stack[-1]>=heights[i]:
                continue
            stack.append(heights[i])
            arr[i] = True
        ans = []

        for i in range(n):
            if arr[i]: ans.append(i)
        return ans