class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1: return False

        key = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in key:
                if len(stack) == 0 or stack.pop(-1) != key[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0