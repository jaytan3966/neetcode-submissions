class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        for item in tokens:
            if item.isalnum():
                nums.append(int(item))
            else:
                a, b = nums.pop(), nums.pop()
                if item == "+":
                    nums.append(a+b)
                elif item == "-":
                    nums.append(b-a)
                elif item == "*":
                    nums.append(a*b)
                else:
                    nums.append(int(b/a))
            print(nums)
        
        return nums[0]
