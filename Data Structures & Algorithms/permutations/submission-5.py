class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seen = defaultdict(bool)

        def dfs(comb):
            if len(comb) == n:
                ans.append(comb[:])
                return

            for j in range(n):
                if not seen[j]:
                    seen[j] = True
                    comb.append(nums[j])
                    dfs(comb)
                    comb.pop()
                    seen[j] = False

            return

        dfs([])
        return ans
