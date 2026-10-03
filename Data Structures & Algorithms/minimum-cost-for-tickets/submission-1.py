class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        dp = [0] * n

        for i in range(n):
            one_day = costs[0]
            seven_day = costs[1]
            thirty_day = costs[2]

            if i>0:
                one_day+=dp[i-1]

            j = i
            seven_day = costs[1]
            while j>=0 and days[i]-days[j] < 7:
                j-=1
            if j>= 0:
                seven_day+=dp[j]

            j = i
            thirty_day = costs[2]
            while j>=0 and days[i]-days[j] < 30:
                j-=1
            if j>= 0:
                thirty_day+=dp[j]
            
            dp[i] = min(one_day, seven_day, thirty_day)
        
        return dp[n-1]

