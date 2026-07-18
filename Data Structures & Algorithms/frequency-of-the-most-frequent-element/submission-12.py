class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        ans = 1

        for i in range(n):
            rem = k
            p = i+1
            same = 1
            while p<n:
                if ((nums[p]-nums[p-1])*(p-i))<=rem:
                    rem-=((nums[p]-nums[p-1])*(p-i))
                    p+=1
                    same+=1
                    print(i, p)
                else: break
            ans = max(ans, same)
        return ans

        