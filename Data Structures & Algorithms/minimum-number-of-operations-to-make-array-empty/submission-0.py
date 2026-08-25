class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ans = 0

        for count in counts:
            if count == 1: return -1
            
            times = count//3
            rem = count%3

            if rem == 1 or rem == 2:
                times+=1
            ans+=times

        return ans
            