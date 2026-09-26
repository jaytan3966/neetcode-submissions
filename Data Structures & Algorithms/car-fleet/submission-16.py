class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]

        pairs.sort(reverse=True)

        ans = []

        for p, s in pairs:
            time = (target-p)/s

            if not ans or ans[-1]<time:
                ans.append(time)
            
        return len(ans)