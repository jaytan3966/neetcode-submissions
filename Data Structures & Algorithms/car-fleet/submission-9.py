class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in list(zip(position, speed))]
        pairs.sort(reverse=True)

        stack = []

        for p, s in pairs:
            time = (target-p)/s

            while stack and stack[-1]>=time:
                stack.pop()
            stack.append(time)
        return len(stack)
        