class MinStack:

    def __init__(self):
        # we will need 2 stacks
        # for stack, we do push, pop, top
        # for min_stack, we also do push, and pop, not top, but we will use it to getMin
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # for push, simply add them to the stack
        self.stack.append(value)

        # for min_stack, we want the smallest element always in the last position
        # if no items, add val directly
        if not self.min_stack:
            self.min_stack.append(value)
        # else, add the min to the end
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))

    def pop(self) -> None:
        # for pop, we want to remove the element on the top
        del self.stack[-1]
        del self.min_stack[-1]        

    def top(self) -> int:
        # for top, simply return top of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # for getMin, use min_stack, return last element which always min
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()