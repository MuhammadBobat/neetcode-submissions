class Solution:
    def isValid(self, s: str) -> bool:  
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')':
                    if stack.pop() != '(': return False
                elif char == '}':
                    if stack.pop() != '{': return False
                elif char == ']':
                    if stack.pop() != '[': return False
                
        if not stack:
            return True
        return False

        
