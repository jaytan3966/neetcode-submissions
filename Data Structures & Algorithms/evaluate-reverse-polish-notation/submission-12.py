class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = {"+": 0, "-": 0, "/":0, "*":0}
        for token in tokens:
            if token not in opers:
                stack.append(token)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                equation = num1+token+num2
                ans = eval(equation)
                stack.append(str(ans))
        return int(stack.pop())