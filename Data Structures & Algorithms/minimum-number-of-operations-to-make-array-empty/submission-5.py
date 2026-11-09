class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ans = 0
        for num in counts:
            while counts[num] != 0:
                if counts[num] == 1:
                    return -1
                if counts[num]%3 == 0:
                    counts[num]-=3
                else:
                    counts[num]-=2
                ans+=1
        return ans