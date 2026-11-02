class Solution:
    def isValid(self, s: str) -> bool:
        # given a string s, containing just left and right parentheses
        # valid date if s is valid
        # 1) open parentheses must be closed by the same type
        # 2) open parentheses must be closed in the correct order
        # 3) Every close parentheses has a corresponding open bracket of same type

        # Logic, make a dictionary, storing the corresponding parentheses pairs
        # d = {x1:x2, y1:y2,...}
        # if left parentheses
        # must be closed, but can be (()), can be left and left and left, ..., as long as they close

        # if right parentheses, it has to close the previous latest parentheses, and pop it
        # at the end, will make empty list []

        d = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in d.keys():
                stack.append(char)
            
            elif char in d.values():
                # case when there is no left parentheses
                if stack == []:
                    return False
                # get the latest left bracket
                top = stack.pop()
                # check if match
                if d[top] != char:
                    return False
        return stack == []

