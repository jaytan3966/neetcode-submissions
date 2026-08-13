class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        diffs = [(abs(arr[i]-x),i) for i in range(n)]

        diffs.sort()
        ans = []
        for i in range(k):
            ans.append(arr[diffs[i][1]])
        ans.sort()
        return ans

