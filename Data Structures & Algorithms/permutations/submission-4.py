class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seen = set()

        def dfs(comb):
            if len(comb) == n:
                ans.append(comb[:])
                return

            for j in range(n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    comb.append(nums[j])
                    dfs(comb)
                    comb.pop()
                    seen.remove(nums[j])

            return

        dfs([])
        return ans
