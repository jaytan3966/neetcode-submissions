class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, len(prices)-1
        prof = 0
        while left<right:
            prof = max(prof, prices[right]-prices[left])
            if prices[left]>prices[right]:
                left+=1
            else:
                right-=1
        return prof
