class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        pref = 0
        ans = 0
        for n in nums:
            pref = (pref+n)%k

            ans+=h[pref]

            h[pref]+=1
        
        print(h)
        return ans