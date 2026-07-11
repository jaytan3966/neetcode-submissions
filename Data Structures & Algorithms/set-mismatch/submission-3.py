class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        ans = [-1, -1]

        seen = set()
        for num in nums:
            if num in seen:
                ans[0] = num
                break
            seen.add(num)

        seen = set(nums)
        for i in range(n):
            if i+1 not in seen:
                ans[1] = i+1
                break
        return ans
            