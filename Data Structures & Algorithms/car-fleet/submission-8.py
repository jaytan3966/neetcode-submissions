class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []

        for i in range(n):
            time = (target-position[i])/speed[i]

            if stack and stack[-1]>=time:
                continue
            else:
                stack.append(time)
        return len(stack)