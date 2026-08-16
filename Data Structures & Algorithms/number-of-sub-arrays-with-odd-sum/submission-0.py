class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0

        n = len(arr)
        prefs = [0]*(n+1)


        for i in range(n):
            prefs[i+1] = arr[i]+prefs[i]
        
        for l in range(n):
            for r in range(l,n+1):
                if (prefs[r]-prefs[l])%2 == 1:
                    ans+=1
        return ans%(10**9 + 7)