class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        seen = set()
        n = len(position)
        
        for i in range(n):
            time = (target-position[i])/speed[i]
            if time not in seen: seen.add(time)
        return len(seen)
