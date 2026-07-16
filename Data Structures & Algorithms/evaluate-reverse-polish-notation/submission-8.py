class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item.isalnum():
                nums.append(int(item))
                print(nums)
            else:
                a, b = nums.pop(), nums.pop()
                if item == "+":
                    nums.append(a+b)
                elif item == "-":
                    nums.append(b-a)
                elif item == "*":
                    nums.append(a*b)
                elif item == "/":
                    nums.append(int(b/a))
            
        
        return nums[0]
