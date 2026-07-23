class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curVal = 1
        preArr = []

        for num in nums:
            preArr.append(curVal)
            curVal*=num

        curVal = 1
        postArr = []
        for i in range(len(nums)-1, -1, -1):
            preArr[i]*=curVal
            curVal*=nums[i]
        return preArr