class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return set(nums)!=len(nums)