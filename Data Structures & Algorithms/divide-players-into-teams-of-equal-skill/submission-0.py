class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        counts = Counter(skill)

        target = sum(skill)/2

        ans = 0

        for num in skill:
            if counts.get(num,0) == 0:
                continue
                
            if counts.get(int(target-num), 0) == 0:
                return -1
            
            counts[int(target-num)]-=1
            counts[num]-=1

            ans+=(num*int(target-num))
        return ans
