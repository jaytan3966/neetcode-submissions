class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []

        n = len(nums)

        counts = Counter(nums)

        for num in counts:
            if counts[num] > math.floor(n/3):
                ans.append(num)
        return ans