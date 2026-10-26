from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"-", "+", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                if token == "+":
                    stack.append(v1 + v2)
                elif token == "-":
                    stack.append(v2 - v1)
                elif token == "*":
                    stack.append(v2 * v1)
                elif token == "/":
                    stack.append(math.trunc(v2 / v1))
            
        return stack[0]
                
