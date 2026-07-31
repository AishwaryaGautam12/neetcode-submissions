class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []

        for i in s:
            if i in ('{','(','['):
                stack.append(i)
                continue
            if i == '}' and (len(stack) == 0 or stack[-1] != '{'):
                return False
            elif i == ')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            elif i == ']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            stack.pop()

        return True if len(stack) == 0 else False