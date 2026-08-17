class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        dom = nums[0]

        for num in counts:
            if counts[num]*2>=n: 
                dom = num
                break
        
        l,r = 0,n
        cur = 0
        for i in range(n):
            l+=1
            r-=1
            if nums[i] == dom: cur+=1

            if cur*2>l and (counts[dom]-cur)*2>r: return i
            
        return -1