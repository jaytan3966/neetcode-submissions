class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()

        for i in range(len(nums)-1):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            print(nums, i)
            l, r = i+1, len(nums)-1
            complement = 0-nums[i]
            while l<r:
                left = nums[l]
                right = nums[r]
                total = left + right
                print(total, complement)
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