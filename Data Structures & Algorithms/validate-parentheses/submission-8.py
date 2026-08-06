class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        pairs = {')':'(', "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if stack and pairs[char] != stack.pop():
                    return False
        return len(stack)==0
