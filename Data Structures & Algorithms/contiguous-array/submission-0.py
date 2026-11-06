class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_indicies = {0:-1}

        n = len(nums)
        pref = 0
        ans = 0
        for i in range(n):
            pref+=(1 if nums[i] == 1 else -1)

            if pref in balance_indicies:
                ans = max(ans, i-balance_indicies[pref])
            else:
                balance_indicies[pref] = i
        return ans


