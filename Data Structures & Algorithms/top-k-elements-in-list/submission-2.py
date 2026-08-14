class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count = Counter(nums)
        # found = set()
        # ans = []

        # while len(ans) != k:
        #     greatest = 0
        #     greatestNum = None
        #     for num in count:
        #         if count[num] > greatest and num not in found:
        #             greatest = count[num]
        #             greatestNum = num
        #     ans.append(greatestNum)
        #     found.add(greatestNum)

        # return ans

        hmap = Counter(nums)
        count = [[] for i in range(len(nums)+1)]
        ans = []
        
        for num in hmap:
            count[hmap[num]].append(num)
            
        for arr in count[::-1]:
            for item in arr:
                ans.append(item)
                k-=1
                if k == 0:
                    return ans



