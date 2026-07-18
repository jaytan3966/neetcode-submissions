class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0

        left = 0
        ans = 1
        for right in range(n):
            total+=nums[right]

            if ((right-left+1)*nums[right])-total>k:
                total-=nums[left]
                left+=1
            
            ans = max(ans, right-left+1)
            print(left, right, ans)
        return ans
        
