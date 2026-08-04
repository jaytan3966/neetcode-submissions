class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = -1
        curLargest = float('-inf')

        while l<=r:
            mid = (l+r)//2
            if nums[mid]>curLargest:
                ans = mid
                curLargest = nums[mid]
                l = mid+1
            else:
                r = mid-1
        return ans