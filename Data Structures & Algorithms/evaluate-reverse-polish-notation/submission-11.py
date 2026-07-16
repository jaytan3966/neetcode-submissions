class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item == "+":
                a, b = nums.pop(), nums.pop()
                nums.append(a+b)
            elif item == "-":
                a, b = nums.pop(), nums.pop()
                nums.append(b-a)
            elif item == "*":
                a, b = nums.pop(), nums.pop()
                nums.append(a*b)
            elif item == "/":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b/a))
            else:
                nums.append(int(item))
        print(nums)
            
        
        return nums[0]
