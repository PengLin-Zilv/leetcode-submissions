class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # store (prev_char,k)
        # then when we met ], we will make prev + k * cur

        cur, num = "", 0
        # initialize cur and num, cur stores the current characters, num will be the k

        for c in s:

            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                # when c = left bracket, we clear the cur and num, append them into stack
                stack.append((cur, num))
                cur, num = "", 0

            elif c == "]":
                # when c = right bracket, we do the opeartion
                prev, k = stack.pop()
                cur = prev + k * cur
            
            else:
                cur += c
        return cur