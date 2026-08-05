class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1: return False
        
        key = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in key:
                if stack.pop(-1) != key[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return True