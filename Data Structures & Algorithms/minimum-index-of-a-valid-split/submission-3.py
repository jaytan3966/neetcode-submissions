class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)

        dom = None
        for num in counts:
            if counts[num] > n//2:
                dom = num
                break
        if not dom: return -1

        left_size = 0
        right_size = n
        left_cnt = 0
        right_cnt = counts[num]
        for i in range(n):
            left_size+=1
            right_size-=1
            if nums[i] == dom:
                left_cnt+=1
                right_cnt-=1
            
            if left_cnt > left_size//2 and right_cnt > right_size//2:
                return i
        return -1