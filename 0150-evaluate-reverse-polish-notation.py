class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # given tokens: they are valid expression in PRN
        # example ["2", "1", "+", "3", "*"]
        # logic: when we meet operations: left opeartion right, push to stack, continue, ...
        # +, -, *, /
        # return the final calculated int

        # note: division will always truncates towards 0, so use int(left / right)

        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # if token is an operation
                # we had 2 num in stack already, get left and right
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    # operation = /
                    result = int(left/right)
                stack.append(result)

            else:
                # token is a num
                stack.append(int(token))

        return stack[-1]