class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if pairs[char] != stack.pop():
                    return False
        return True
