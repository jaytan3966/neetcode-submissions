class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []


        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: continue

            l, r = i+1, len(nums)-1
            compl = -nums[i]

            while l<r:
                if nums[l] + nums[r] > compl: r-=1
                elif nums[l] + nums[r] < compl: l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l<r and nums[l] == nums[l-1]: l+=1    
                    
        return ans