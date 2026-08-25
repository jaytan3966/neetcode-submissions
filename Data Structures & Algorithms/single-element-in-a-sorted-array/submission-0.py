class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for n in nums:
            if counts[n] == 1: return n
