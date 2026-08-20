class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums)-2:
            first = nums[i]
            l, r = i+1, len(nums)-1
            complement = 0-first
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
            i+=1
            while nums[i] == first:
                i+=1
        return ans