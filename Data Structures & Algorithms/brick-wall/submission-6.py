class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        n = len(wall)
        table = defaultdict(int)

        for r in range(n):
            cur = 0
            for i in range(len(wall[r])-1):
                cur+=wall[r][i]
                table[cur]+=1
        
        greatest_count = 0
        for num in table:
            if table[num]>greatest_count:
                greatest_count = table[num]

        return n-greatest_count