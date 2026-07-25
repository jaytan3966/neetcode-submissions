class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        total = sum(a for a,b in costs)

        diffs = sorted(b-a for a, b in costs)

        total+=sum(diffs[:n])

        return total

