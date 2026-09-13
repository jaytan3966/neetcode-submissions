class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0]*2 for _ in range(n+1)]
        ans = 0
        dp[1][True] = -prices[0]
        dp[1][False] = 0

        #[0,0] --> [max profit if buying, max profit of not buying at day i]
        for i in range(1, n):
            for buying in [True, False]:

                #buying
                if buying:
                    dp[i+1][buying] = max(dp[i-1][False]-prices[i], dp[i][True])
                
                #selling
                else:
                    dp[i+1][buying] = max(dp[i][False] , dp[i][True] + prices[i])

                if dp[i+1][buying]>ans: ans = dp[i+1][buying]
        
        return ans
