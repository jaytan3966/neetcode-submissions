class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        maxP = 0
        while right<len(prices):
            if prices[left] < prices[right]:
                maxP = max(prices[right]-prices[left], maxP)
            else:
                left = right
            right+=1
        return maxP
