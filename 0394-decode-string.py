class Solution:
    def decodeString(self, s: str) -> str:
        # core logic: we might meet [] in [],
        # so we always want to solve inner first
        # example "3[a2[c]]"
        # we'd like, when we meet first ], get the acc, then apply it with 3

        # use stack, to store (prev_str, num)
        # when we meet number, store it to cur_num
        # when we meet "[", save the outside, to stack, clear cur_str and cur_num
        # when we meet "]", this layer is ended, calculate cur_str
        # else, cur_str += c

        stack = []
        cur_str = ""
        cur_num = 0

        for c in s:
            if c.isdigit():
                # maynot be single digit
                cur_num = cur_num * 10 + int(c)

            elif c == "[":
                # means we will meet inner letters
                # need to store outer letters and num into stack
                stack.append((cur_str, cur_num))
                cur_str, cur_num = "", 0
            elif c == "]":
                # means inner loop ended
                prev_str, num = stack.pop()
                cur_str = prev_str + cur_str * num

            else:
                cur_str += c

        return cur_str

