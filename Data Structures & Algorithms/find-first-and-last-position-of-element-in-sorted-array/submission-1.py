class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        l, r = 0, len(nums)-1
        def binary_search(l,r, left):
            nonlocal ans
            while l<=r:
                mid = (l+r)//2

                if nums[mid] == target:
                    if left: 
                        ans[0] = mid
                        r = mid-1
                    else: 
                        ans[1] = mid
                        l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l=mid+1
        binary_search(l,r,True)
        binary_search(l,r,False)
                
        return ans