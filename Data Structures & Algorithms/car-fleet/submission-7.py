class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in list(zip(position, speed))]
        pairs.sort(reverse=True)
        stack = []

        print(pairs)

        for p, s in pairs:
            stack.append((target-p)/s)
            while len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)