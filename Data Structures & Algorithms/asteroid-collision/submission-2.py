class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while stack and stack[-1]/num < 0:             
                last = stack.pop()
                if abs(last)<abs(num):
                    stack.append(num)
                elif abs(last)>abs(num):
                    stack.append(last)
                    break
                else: break
            else:
                stack.append(num)
        return stack