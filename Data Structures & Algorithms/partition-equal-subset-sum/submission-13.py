class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        target = total//2
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]

        for _ in range(n+1):
            dp[_][0] = True

        for l in range(1, n+1):
            for rem in range(1, target+1):
                if nums[l]<=rem:
                    dp[l][rem] = dp[l][rem] or dp[l-1][rem-nums[l]]
                else:
                    dp[l][rem] = dp[l-1][rem]
            if dp[l][target]: return True
        return False




