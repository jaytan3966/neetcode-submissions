class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        ans = 0
        n = len(nums)
        
        for i, jmp in enumerate(nums):

            if i+jmp>farthest:
                ans+=1
            farthest = max(farthest, i+jmp)
            if farthest == n-1: return ans
        return ans

