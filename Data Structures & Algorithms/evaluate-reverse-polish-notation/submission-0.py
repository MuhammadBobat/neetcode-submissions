import math
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(math.trunc(num2 / num1))
        
        return stack[-1]

