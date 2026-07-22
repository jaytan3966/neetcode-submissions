class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in list(zip(position, speed))]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            while stack and stack[-1]>=(target-p)/s:
                stack.pop()
            stack.append((target-p)/s)
        return len(stack)