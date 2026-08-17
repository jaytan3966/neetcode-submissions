class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0

        even = 1
        odd = 0
        pref = 0

        for num in arr:
            pref += num
            if pref%2:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1

        return ans%(10**9 + 7)