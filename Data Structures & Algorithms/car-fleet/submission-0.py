class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = set()
        for i in range(len(position)):
            fleets.add((target-position[i])//speed[i])

        return len(fleets)