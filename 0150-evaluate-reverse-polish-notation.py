class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # valid operations: "+", "-", "*", "/"
        # for /, we should do floor division and then return to int, int(x/y)

        # logic: when we meet an opration, we do them with the most recently added 2 numbers
        # we pop 2 numbers: y = pop(), x = pop(), 
        # and then x operation y, add this to the list
        # continues, ...

        # we add numbers into a stack
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                y = stack.pop()
                x = stack.pop()     
            # if token is an operator
            # we pop, pop, compute, then put it back
                if token == "+":
                    result = x + y
                elif token == "-":
                    result = x - y
                elif token == "*":
                    result = x * y
                else:
                    result = int(x/y)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

