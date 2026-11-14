class MinStack:
    # min stack, supports push/pop/top/getMin, all in O(1)
    # a simple way to achieve so is using 2 stack, 1 for push/pop/top, 1 also push and pop, but getMin
    def __init__(self):
        self.stack = []
        self.min_stack = []
        # min stack will compare the new value with current smallest(last element), push at the end of list,
        # so we can pop it as O(1)

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            # if min_stack empty, add value
            self.min_stack.append(value)
        else:
            # if has value, compare and append the min value
            self.min_stack.append(min(value, self.min_stack[-1]))


    def pop(self) -> None:
        # we will pop for both stack
        # remove top element of the stack
        # for min stack, we pop because we dont want to keep a element that is supposed to be poped as min value
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        # get top element of the stack
        # simply return top of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # get min element
        # simply return top of the min_stack
        return self.min_stack[-1]


