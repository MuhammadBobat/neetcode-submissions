class Solution:
    def isValid(self, s: str) -> bool:  
        openToClose = {
            "{":"}",
            "(":")", 
            "[":"]"
        }
        stack = []

        for char in s:
            if char in openToClose:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack and openToClose[stack[-1]] != char:
                    return False

                stack.pop()
                
        if not stack:
            return True

        return False