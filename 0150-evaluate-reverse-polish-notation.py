class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # tokens are numbers or operators
        # we want to evaluate reverse Polish notation
        # valid operations are +, -, *, /

        # for example 3 5 +, becomes 3 + 5, so when we met operation:
        # left operates right
        # right = stack.pop()
        # left = stack.pop() # second last item near the operation
        # and then repeat, it is guranteed to be a valid expression

        # first we want a stack, to add token

        stack = []

        for token in tokens:
            # two cases:
            # 1. operations: "+", "-", "*", "/" - so we find left and right, operate, add them back to stack
            # 2. number, add to the stack
            if token in ("+", "-", "*", "/"):
                right = int(stack.pop())
                left = int(stack.pop())
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                elif token == "/":
                    # always truncates toward 0
                    result = int(left / right)
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[0]