class Solution:
    def decodeString(self, s: str) -> str:
        num, string = 0, ""
        # num keeps track of the num
        # string keeps track of current string (will be pushed to stack each time sees "[")

        stack = [] # keep track of the prev string and pop() after "]" to get the most inner decoding string

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                # num can be [1,300]
            elif c == "[":
                # if c is left bracket, append current string and num into stack, wait for "]" to pop
                stack.append((num, string))
                num, string = 0, ""
            elif c == "]":
                # if c is right bracket, k and prev = pop()
                # add them into string
                k, prev = stack.pop()
                string = prev + k*string

            else:
                # if c is a letter
                # add to string
                string += c
        return string