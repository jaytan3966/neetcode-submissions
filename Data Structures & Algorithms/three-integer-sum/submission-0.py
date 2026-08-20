class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        seen = set()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            compl = -nums[i]
            while l<r:
                if nums[l] + nums[r] > compl: r-=1
                elif nums[l] + nums[r] < compl: l+=1
                else:
                    if tuple([nums[i], nums[l], nums[r]]) in seen:
                        pass
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        seen.add(tuple([nums[i], nums[l], nums[r]]))
                    l, r = l+1, r-1     
                    
        return ans