class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        n = len(path)

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(part)

        return "/" + "/".join(stack)
            
