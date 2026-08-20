class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            complement = 0-nums[i]
            while l<r:
                left = nums[l]
                right = nums[r]
                total = left + right
                if total>complement:
                    r-=1
                elif total<complement:
                    l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                while l<r and nums[l] == left:
                    l+=1
                while l<r and nums[r] == right:
                    r-=1
        return ans