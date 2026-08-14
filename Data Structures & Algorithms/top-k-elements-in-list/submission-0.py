class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        nums.sort()
        count = Counter(nums)
        found = set()
        ans = []

        while len(ans) != k:
            greatest = 0
            greatestNum = None
            for num in count:
                if count[num] > greatest and num not in found:
                    greatest = count[num]
                    greatestNum = num
            ans.append(greatestNum)
            found.add(greatestNum)

        return ans




