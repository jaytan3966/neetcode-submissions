class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i<j:
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid
        pivot = i
        
        def binary_search(i: int, j: int) -> int:
            while i<=j:
                mid = (i+j)//2
                if nums[mid]>target:
                    j = mid -1
                elif nums[mid]<target:
                    i = mid+1
                else:
                    return mid
            return -1
        
        result = binary_search(0, pivot-1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums)-1)
