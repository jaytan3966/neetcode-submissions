class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        ans = 0
        curEnd = 0

        for i, jmp in enumerate(nums[:-1]):
            farthest = max(farthest, i+jmp)
            
            if i == curEnd:
                ans+=1
                curEnd = farthest
        return ans

