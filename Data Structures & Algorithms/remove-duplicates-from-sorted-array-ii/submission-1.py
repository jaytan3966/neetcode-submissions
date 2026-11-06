class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        left = right = 0

        cur_num = nums[0]
        cur_cnt = 0

        n = len(nums)
        while right<n:
            num = nums[right]

            if num == cur_num:
                cur_cnt+=1
            else:
                cur_num = num
                cur_cnt = 1
            
            if cur_cnt <= 2:
                nums[left] = num
                left+=1
            right+=1
        return left