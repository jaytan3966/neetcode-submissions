class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        evens = 1
        odds = 0

        pre = 0

        for num in arr:
            pre+=num

            if pre%2:
                ans+=evens
                odds+=1
            else:
                ans+=odds
                evens+=1
        return ans