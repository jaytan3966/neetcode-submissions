class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        ans = 1

        for i in range(n):
            if i<n-1 and nums[i] == nums[i+1]: continue
            rem = k
            p = i+1
            same = 1
            while rem>0:
                if p<n and (nums[p]-nums[i])<=rem:
                    rem-=(nums[p]-nums[i])
                    p+=1
                    same+=1
                    print(i, p)
                else: break
            ans = max(ans, same)
        return ans

        