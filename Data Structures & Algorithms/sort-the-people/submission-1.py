class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        pairs = {}
        for i in range(len(names)):
            pairs[heights[i]] = names[i]

        height = list(pairs.keys())
        height.sort(reverse=True)

        ans = []
        for h in height:
            ans.append(pairs[h])
        return ans