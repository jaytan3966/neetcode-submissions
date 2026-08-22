class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = 0, 0
        ans = 0

        while l<r:
            if height[l]>maxL: maxL = height[l]
            if height[r]>maxR: maxR = height[r]

            if maxL<maxR:
                ans+=(maxL-height[l])
                l+=1
            else:
                ans+=(maxR-height[r])
                r-=1
        return ans
    