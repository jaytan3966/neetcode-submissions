class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        seen = set()
        def backtrack(curr):
            if len(curr) == n:
                ans.append(curr[:])
                return
            for i in range(n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    seen.remove(nums[i])
            return
        backtrack([])
        return ans