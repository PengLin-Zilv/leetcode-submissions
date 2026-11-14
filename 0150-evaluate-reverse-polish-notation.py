class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # given tokens: a list of strings, representing an valid expression in RPN
        # example tokens = ["2", "1", "+", "3", "*"]
        # rule is left (second pop()) do operation to the right (first pop())

        # / -> truncates to 0 which means use / which gives a float, and int() to truncates towards 0
        # the input will always be valid arithmetic expression in a RPN

        # for each num, add to the stack
        # for each opeartion, get left and right, do corresponding opeartion with them

        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # we met operations, there is at least 2 number ahead of us
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                elif token == "/":
                    result = int(left / right)
                stack.append(result)

            else:
                # token is a string format of number, add the number
                stack.append(int(token))
        return stack[0]