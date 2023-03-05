class Solution:
    def eval_cal(self, operator, first, second):
        if operator == '+':
            return first + second
        elif operator == '-':
            return first - second
        elif operator == '*':
            return first * second
        else:
            return int(first / second)
            
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
                stack.append(self.eval_cal(token, first, second))
            else:
                stack.append(int(token))

        return stack[0]