class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = {}
        n = len(nums)

        for num in nums:
            seen[num] = False

        def dfs(comb):
            if len(comb) == n:
                ans.append(comb[:])
                return
            
            for num in nums:
                if not seen[num]:
                    seen[num] = True

                    comb.append(num)

                    dfs(comb)

                    comb.pop()

                    seen[num] = False
                
            return
        dfs([])
        return ans