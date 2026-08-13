class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prof = 0
        for i in range(len(prices)):
            r = i+1

            while r<len(prices):
                prof = max(prices[r]-prices[i], prof)
                r+=1
        return prof