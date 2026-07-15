class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = defaultdict(bool)

        def dfs(i, comb):
            if len(comb) == n:
                ans.append(comb[:])
                return

            for r in range(n):
                if not used[nums[r]]:
                    used[nums[r]] = True
                    comb.append(nums[r])
                    dfs(r+1, comb)
                    comb.pop()
                    used[nums[r]] = False

        dfs(0, [])
        return ans