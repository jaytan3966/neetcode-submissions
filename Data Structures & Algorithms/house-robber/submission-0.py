class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        past = []
        most = 0
        for i in range(n):
            largest = 0
            for l in range(0,i-1):
                if past[l]>largest:
                    largest = past[l]
            past.append(nums[i]+largest)
            most = nums[i] + largest if nums[i]+largest > most else most

        return most