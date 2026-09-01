class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        htable = {x: i for i, x in enumerate(nums)}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in htable:
                return [i, htable[compl]]