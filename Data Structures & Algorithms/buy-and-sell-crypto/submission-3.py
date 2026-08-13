class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        smallest = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-smallest)
            smallest = min(smallest, prices[i])
        return profit