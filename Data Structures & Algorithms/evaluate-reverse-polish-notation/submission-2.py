class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item.isalnum():
                nums.append(int(item))
            else:
                if item == "+":
                    nums.append(nums.pop()+nums.pop())
                elif item == "-":
                    nums.append(nums.pop()-nums.pop())
                elif item == "*":
                    nums.append(nums.pop()*nums.pop())
                else:
                    nums.append(nums.pop()/nums.pop())
            print(nums)
        
        return nums[0]
