class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        target = total//2
        n = len(nums)
        dp = [False for _ in range(target+1)]
        dp[0] = True

        for l in range(n):
            for rem in range(1, target+1):
                if nums[l]<=rem:
                    dp[rem] = dp[rem] or dp[rem-nums[l]]
                if dp[target]: return dp[target]
        print(dp)
        return False



