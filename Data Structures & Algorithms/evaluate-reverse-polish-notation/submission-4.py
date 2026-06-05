class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == '+':
                stack[-2] = stack[-2] + stack[-1]
                stack = stack[:-1]
            elif token == '-':
                stack[-2] = stack[-2] - stack[-1]
                stack = stack[:-1]
            elif token == '*':
                stack[-2] = stack[-2] * stack[-1]
                stack = stack[:-1]
            elif token == '/':
                stack[-2] = int(stack[-2] / stack[-1])
                stack = stack[:-1]
            else:
                stack.append(int(token))
            print(stack)
            
        return int(stack[0])