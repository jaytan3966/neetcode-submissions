class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[l]<=target<=nums[r]:
                if nums[mid] == target: return mid
                elif nums[mid]>target: r = mid-1
                else: l = mid+1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]: r = mid
                else: l = mid+1
            else:
                if nums[mid]<=target<=nums[r]: l = mid
                else: r=mid-1

        return -1