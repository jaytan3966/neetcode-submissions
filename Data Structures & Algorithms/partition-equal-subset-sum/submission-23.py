class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        
        if total%2: return False

        target = total//2
        n = len(nums)

        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for cur in range(1, target+1):
                if nums[i-1]<=cur:
                    dp[i][cur] = dp[i-1][cur-nums[i-1]] or dp[i-1][cur]
        
        return dp[n][target]