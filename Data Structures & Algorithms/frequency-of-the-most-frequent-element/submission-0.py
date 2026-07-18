class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        ans = 1

        for i in range(n):
            rem = k
            p = i
            same = 1
            while rem>0:
                if p<n-1 and (nums[p+1]-nums[p])*(p+1)<=rem:
                    rem-=((nums[p+1]-nums[p])*(p+1))
                    p+=1
                    same+=1
                else: break
            ans = max(ans, same)
        return ans

        