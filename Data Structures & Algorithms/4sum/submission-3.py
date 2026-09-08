class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        seen = set()

        for a in range(n-3):

            if a>0 and nums[a] == nums[a-1]: continue

            for b in range(a+1, n-2):

                c, d = b+1, n-1
                
                while c<d:
                    total = nums[a]+nums[b]+nums[c]+nums[d]

                    if total == target:
                        if (nums[a], nums[b], nums[c], nums[d]) not in seen:
                            ans.append([nums[a], nums[b], nums[c], nums[d]])
                            seen.add((nums[a], nums[b], nums[c], nums[d]))
                        c+=1
                        while c<d and nums[c]==nums[c-1]: c+=1
                    elif total>target:
                        d-=1
                        while c<d and nums[d]==nums[d+1]: d-=1
                    else:
                        c+=1
                        while c<d and nums[c]==nums[c-1]: c+=1
        return ans
