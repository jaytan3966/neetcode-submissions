class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        seen = set()

        def dfs(cur, r):
            nonlocal ans

            if r > n: return

            ans.append(cur[:])
            r+=1

            for i in range(r, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    cur.append(nums[i])
                    dfs(cur, i)
                    cur.pop()
                    seen.remove(nums[i])
            return

        dfs([], -1)
        return ans


