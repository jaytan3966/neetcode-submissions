class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        low = prices[0]
        
        for i in range(len(prices)):
            ans = max(ans, prices[i]-low)
            low = min(low, prices[i])
        return ans