class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights)-1

        while l<r:
            prod = (r-l) * min(heights[l], heights[r])
            ans = max(ans, prod)
            if heights[l+1] > heights[l]: l+=1
            else: r-=1
        return ans