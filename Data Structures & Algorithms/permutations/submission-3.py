class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = defaultdict(bool)

        def dfs(comb):
            if len(comb) == n:
                ans.append(comb[:])
                return

            for i in range(n):
                if not used[nums[i]]:
                    used[nums[i]] = True
                    comb.append(nums[i])
                    dfs(comb)
                    comb.pop()
                    used[nums[i]] = False

        dfs([])
        return ans