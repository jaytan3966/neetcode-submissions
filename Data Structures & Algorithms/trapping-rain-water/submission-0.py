class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]

        ans = 0

        while l<r:
            if maxL<maxR:
                if maxL-height[l]>0:
                    ans+=maxL-height[l]
                l+=1
                maxL = max(maxL, height[l])
            else:
                if maxR-height[r]>0:
                    ans+=maxR-height[r]
                r-=1
                maxR = max(maxR, height[r])
        return ans