class Solution:
    def isValid(self, s: str) -> bool:
        # valid parentheses: given string s
        # it only contains "(", ")", "[", "]", "{", "}"
        # determine if valid
        # valid if: 
        # 1) open brackets must be closed by same type of bracket
        # 2) must be closed in the correct order: like this "()[]" or "{()}"
        # 3) every close bracket has a corresponding open bracket of the same type, so "()}" invalid, ")" alone is also invalid, so need to check if we met close bracket first and it will be invalid

        # we will use stack, the first thing is to make dictionary, key is the left paren, and value is its corresponding right bracket

        d = {"(": ")", "[": "]", "{": "}"}
        stack = []

        # next we look through each bracket in the string, see if they are left or right
        # if left(key), we want to add them to a stack list, we want to verify and pop them when we met right(value)

        for char in s:
            if char in d.keys():
                # left bracket, we add them to the stack
                stack.append(char)

            elif char in d.values():
                # first we check if stack is empty, if so return False becaue we cant have right bracket alone
                if not stack:
                    return False
                # we check the last item in stack match with the right bracket? because we want to close it
                top = stack.pop()
                # we got the item already, see if match in dictionary
                if d[top] != char:
                    return False
                # so it will return False if unmatch, then we will need to pop everything and so stack will eventually be empty, if so return True
        return True if stack == [] else False