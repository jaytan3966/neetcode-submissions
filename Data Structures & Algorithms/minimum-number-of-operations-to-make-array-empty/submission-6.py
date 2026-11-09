class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ans = 0
        for num in counts:
            if counts[num] == 1:
                return -1
            ans+=((counts[num]+2)//3)
        return ans