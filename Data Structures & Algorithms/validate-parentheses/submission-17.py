class Solution:
    def isValid(self, s: str) -> bool:  
        openToClose = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []

        for char in s:
            if char in openToClose:
                stack.append(char)
            else:
                if stack and char == openToClose[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        
        return False
