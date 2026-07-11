class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        ans = []
        n, m = len(firstList), len(secondList)

        while l<n and r<m:
            first, second = firstList[l], secondList[r]

            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if start<=end: ans.append([start,end])

            if first[1]<second[1]: l+=1
            else: r+=1
        return ans