class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        target = total//2
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n)]

        for _ in range(n):
            dp[_][0] = True

        for l in range(n):
            for rem in range(1, target+1):
                if nums[l]<=rem:
                    dp[l][rem] = dp[l-1][rem-nums[l]]
                if rem == target and dp[l][rem] == True:
                    return True
        return False



