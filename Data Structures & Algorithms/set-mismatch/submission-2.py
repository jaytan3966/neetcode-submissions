class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        seen = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in seen:
                ans.append(nums[i])
                ans.append(nums[i]+1)
                break
            seen.add(i+1)
        return ans