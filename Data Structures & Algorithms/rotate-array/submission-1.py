class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k%=n

        first = nums[:k]
        second = nums[k:]

        i, j = 0, k
        while j<n:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j+=1