class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openToClose = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        # Iterate through the string, push opens onto stack, pop on closes
        for char in s:
            if char in openToClose.keys():
                stack.append(char)
            
            else:
                if stack and openToClose[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False