class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item == "+":
                a, b = nums.pop(), nums.pop()
                nums.append(int(a)+int(b))
            elif item == "-":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b)-int(a))
            elif item == "*":
                a, b = nums.pop(), nums.pop()
                nums.append(int(a)*int(b))
            elif item == "/":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b)//int(a))
            else:
                nums.append(item)
            
        
        return nums[0]
