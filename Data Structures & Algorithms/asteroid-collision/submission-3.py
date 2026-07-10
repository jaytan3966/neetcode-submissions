class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while stack and num < 0 < stack[-1]:             
                if abs(num)>stack[-1]:
                    stack.pop()
                elif abs(num) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)
        return stack