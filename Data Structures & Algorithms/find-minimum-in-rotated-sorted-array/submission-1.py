class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        ans = nums[0]

        while i<=j:
            mid = (i+j)//2
            if nums[mid] > nums[j]:
                i = mid+1
            elif nums[mid] < nums[i]:
                j = mid-1
            else:
                if j<len(nums):
                    return nums[j+1]
                else:
                    return nums[i]
        return ans