class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []

        for i in s:
            if i in ('{','(','['):
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            elif i == '}' and stack[-1] != '{':
                return False
            elif i == ')' and stack[-1] != '(':
                return False
            elif i == ']' and stack[-1] != '[':
                return False
            stack.pop()

        return True if len(stack) == 0 else False