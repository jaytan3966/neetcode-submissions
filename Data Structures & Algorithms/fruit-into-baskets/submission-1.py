class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        counts = defaultdict(int)
        l = 0

        ans = 0
        for r in range(n):
            counts[fruits[r]]+=1

            while len(counts)>2:
                counts[fruits[l]]-=1

                if counts[fruits[l]]==0:
                    del counts[fruits[l]]
                l+=1
            
            ans = max(ans, r-l+1)
        return ans

