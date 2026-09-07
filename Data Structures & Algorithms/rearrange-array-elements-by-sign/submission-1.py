class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n

        l, r = 0, 1

        for num in nums:
            if num>0:
                ans[l] = num
                l+=2
            else:
                ans[r] = num
                r+=2
        return ans