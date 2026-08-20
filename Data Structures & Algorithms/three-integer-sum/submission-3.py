class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums)-2:
            while nums[i] == nums[i-1] and i < len(nums)-2:
                i+=1
            j, k = i+1, len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
            i+=1
        return ans
                
