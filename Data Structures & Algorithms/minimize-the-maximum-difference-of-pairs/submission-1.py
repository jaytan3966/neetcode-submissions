class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def canMake(maxDiff):
            pairs = 0
            i = 1

            while i < len(nums):
                if nums[i] - nums[i - 1] <= maxDiff:
                    pairs += 1
                    i += 2
                else:
                    i += 1

                if pairs >= p:
                    return True

            return False

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left