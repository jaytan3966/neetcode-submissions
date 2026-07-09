class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        odd, even = False, False
        for i in range(n-1):
            if (nums[i]%2 and not nums[i+1]%2) or (nums[i+1]%2 and not nums[i1]%2): return True
        return False
