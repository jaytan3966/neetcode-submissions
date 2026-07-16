class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = {"+": 0, "-": 0, "/":0, "*":0}
        for token in tokens:
            if token not in opers:
                stack.append(token)
            else:
                num2 = str(stack.pop())
                num1 = str(stack.pop())
                
                ans = eval(num1+token+num2)
                stack.append(int(ans))
                print(stack)
        return int(stack.pop())