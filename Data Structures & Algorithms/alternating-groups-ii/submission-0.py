class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        circle = colors

        for i in range(k):
            circle.append(colors[i])
        
        length = ans = 0
        for r in range(1, len(circle)):
            if circle[r] != circle[r-1]:
                length+=1
            else:
                length = 1
            
            if length>=k:
                ans+=1
        return ans
            