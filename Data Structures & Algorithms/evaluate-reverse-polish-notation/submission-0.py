class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item.isalnum():
                nums.append(int(item))
            else:
                if item == "+":
                    nums[0] = nums[0] + nums[1]
                elif item == "-":
                    nums[0] = nums[0] - nums[1]
                elif item == "*":
                    nums[0] = nums[0] * nums[1]
                else:
                    nums[0] = nums[0] / nums[1]
                nums.pop(1)
        
        return nums[0]
