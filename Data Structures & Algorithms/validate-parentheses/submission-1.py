class Solution:
    def isValid(self, s: str) -> bool:
        key = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in key:
                if len(stack) == 0 or stack.pop(-1) != key[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return True