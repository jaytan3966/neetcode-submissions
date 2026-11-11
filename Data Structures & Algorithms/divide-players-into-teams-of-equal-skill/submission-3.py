class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        counts = Counter(skill)
        n = len(skill)
        target = (2*sum(skill))//n

        ans = 0

        for num in skill:
            if counts.get(num,0) == 0:
                continue

            if counts.get(target-num, 0) == 0:
                return -1
            
            counts[target-num]-=1
            counts[num]-=1

            ans+=(num*(target-num))
        return ans
