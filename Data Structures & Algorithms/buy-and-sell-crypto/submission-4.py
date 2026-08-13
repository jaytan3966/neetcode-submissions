class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cheapest = prices[0]

        for i in range(len(prices)):
            ans = max(ans, prices[i]-cheapest)
            cheapest = min(prices[i], cheapest)
        return ans