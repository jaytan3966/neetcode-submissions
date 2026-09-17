class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        
        stack = []
        for position, speed in pairs:
            time = (target-position)/speed

            while not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
