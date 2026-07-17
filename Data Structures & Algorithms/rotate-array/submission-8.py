class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        new = n-(k%n)

        i, j = 0, new
        while j<n:
            if i == k: break
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j+=1
        if n%2:
            r = n-1
            while r!=k:
                nums[r], nums[k] = nums[k], nums[r]
                r-=1
                